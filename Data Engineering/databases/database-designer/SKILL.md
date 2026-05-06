---
name: "database-designer"
description: "Use when the user asks to design database schemas, plan data migrations, optimize queries, choose between SQL and NoSQL, or model data relationships."
---

# Database Designer - POWERFUL Tier Skill

## Overview

A comprehensive database design skill that provides expert-level analysis, optimization, and migration capabilities for modern database systems. This skill combines theoretical principles with practical tools to help architects and developers create scalable, performant, and maintainable database schemas.

## Core Competencies

### Schema Design & Analysis
- **Normalization Analysis**: Automated detection of normalization levels (1NF through BCNF)
- **Denormalization Strategy**: Smart recommendations for performance optimization
- **Data Type Optimization**: Identification of inappropriate types and size issues
- **Constraint Analysis**: Missing foreign keys, unique constraints, and null checks
- **Naming Convention Validation**: Consistent table and column naming patterns
- **ERD Generation**: Automatic Mermaid diagram creation from DDL

### Index Optimization
- **Index Gap Analysis**: Identification of missing indexes on foreign keys and query patterns
- **Composite Index Strategy**: Optimal column ordering for multi-column indexes
- **Index Redundancy Detection**: Elimination of overlapping and unused indexes
- **Performance Impact Modeling**: Selectivity estimation and query cost analysis
- **Index Type Selection**: B-tree, hash, partial, covering, and specialized indexes

### Migration Management
- **Zero-Downtime Migrations**: Expand-contract pattern implementation
- **Schema Evolution**: Safe column additions, deletions, and type changes
- **Data Migration Scripts**: Automated data transformation and validation
- **Rollback Strategy**: Complete reversal capabilities with validation
- **Execution Planning**: Ordered migration steps with dependency resolution

## Database Design Principles
→ See references/database-design-reference.md for details
→ See references/full-schema-examples.md for a worked end-to-end example (Task Management SaaS)

## Cross-cutting Schema Concerns

Apply these to every tenant-scoped table from day one — retrofitting is painful:

- **Multi-tenancy**: add `organization_id` to all tenant-scoped tables; enforce isolation via RLS (below) rather than application-level filtering
- **Soft deletes**: add `deleted_at TIMESTAMPTZ` instead of hard `DELETE`; pair with a partial index on `WHERE deleted_at IS NULL`
- **Audit trail**: add `created_by`, `updated_by`, `created_at`, `updated_at`; for regulated domains, also write before/after JSON to a separate audit log
- **Optimistic locking**: add `version INTEGER` for tables with concurrent writers; increment on every update; reject stale writes
- **Surrogate keys**: use UUID/CUID PKs — never email, slug, or business identifiers (those are mutable)

## Best Practices

### Schema Design
1. **Use meaningful names**: Clear, consistent naming conventions
2. **Choose appropriate data types**: Right-sized columns for storage efficiency
3. **Define proper constraints**: Foreign keys, check constraints, unique indexes
4. **Consider future growth**: Plan for scale from the beginning
5. **Document relationships**: Clear foreign key relationships and business rules

### Performance Optimization
1. **Index strategically**: Cover common query patterns without over-indexing
2. **Monitor query performance**: Regular analysis of slow queries
3. **Partition large tables**: Improve query performance and maintenance
4. **Use appropriate isolation levels**: Balance consistency with performance
5. **Implement connection pooling**: Efficient resource utilization

### Security Considerations
1. **Principle of least privilege**: Grant minimal necessary permissions
2. **Encrypt sensitive data**: At rest and in transit
3. **Audit access patterns**: Monitor and log database access
4. **Validate inputs**: Prevent SQL injection attacks
5. **Regular security updates**: Keep database software current
6. **RLS over application-level filtering**: Database enforces tenancy; app code can't be the only line of defense

### Operational Hygiene
1. **Timestamps everywhere**: `created_at` and `updated_at` on every table
2. **Soft deletes for auditable data**: `deleted_at` instead of `DELETE` where history matters
3. **Audit log for compliance**: Log before/after JSON for regulated domains
4. **UUIDs or CUIDs as PKs**: Avoid sequential integer leakage to clients
5. **Index every foreign key**: FK columns without indexes turn `JOIN` into a scan
6. **Partial indexes for active rows**: `WHERE deleted_at IS NULL` keeps index size proportional to live data

## Query Generation Patterns

### SELECT with JOINs

```sql
-- INNER JOIN: only matching rows
SELECT o.id, c.name, o.total
FROM orders o
INNER JOIN customers c ON c.id = o.customer_id;

-- LEFT JOIN: all left rows, NULLs for non-matches
SELECT c.name, COUNT(o.id) AS order_count
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.id
GROUP BY c.name;

-- Self-join: hierarchical data (employees/managers)
SELECT e.name AS employee, m.name AS manager
FROM employees e
LEFT JOIN employees m ON m.id = e.manager_id;
```

### Common Table Expressions (CTEs)

```sql
-- Recursive CTE for org chart
WITH RECURSIVE org AS (
  SELECT id, name, manager_id, 1 AS depth
  FROM employees WHERE manager_id IS NULL
  UNION ALL
  SELECT e.id, e.name, e.manager_id, o.depth + 1
  FROM employees e INNER JOIN org o ON o.id = e.manager_id
)
SELECT * FROM org ORDER BY depth, name;
```

### Window Functions

```sql
-- ROW_NUMBER for pagination / dedup
SELECT *, ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY created_at DESC) AS rn
FROM orders;

-- RANK with gaps, DENSE_RANK without gaps
SELECT name, score, RANK() OVER (ORDER BY score DESC) AS rank FROM leaderboard;

-- LAG/LEAD for comparing adjacent rows
SELECT date, revenue,
  revenue - LAG(revenue) OVER (ORDER BY date) AS daily_change
FROM daily_sales;
```

### Aggregation Patterns

```sql
-- FILTER clause (PostgreSQL) for conditional aggregation
SELECT
  COUNT(*) AS total,
  COUNT(*) FILTER (WHERE status = 'active') AS active,
  AVG(amount) FILTER (WHERE amount > 0) AS avg_positive
FROM accounts;

-- GROUPING SETS for multi-level rollups
SELECT region, product, SUM(revenue)
FROM sales
GROUP BY GROUPING SETS ((region, product), (region), ());
```

---

## Migration Patterns

### Up/Down Migration Scripts

Every migration must have a reversible counterpart. Name files with a timestamp prefix for ordering:

```
migrations/
├── 20260101_000001_create_users.up.sql
├── 20260101_000001_create_users.down.sql
├── 20260115_000002_add_users_email_index.up.sql
└── 20260115_000002_add_users_email_index.down.sql
```

### Zero-Downtime Migrations (Expand/Contract)

Use the expand-contract pattern to avoid locking or breaking running code:

1. **Expand** — add the new column/table (nullable, with default)
2. **Migrate data** — backfill in batches; dual-write from application
3. **Transition** — application reads from new column; stop writing to old
4. **Contract** — drop old column in a follow-up migration

### Data Backfill Strategies

```sql
-- Batch update to avoid long-running locks
UPDATE users SET email_normalized = LOWER(email)
WHERE id IN (SELECT id FROM users WHERE email_normalized IS NULL LIMIT 5000);
-- Repeat in a loop until 0 rows affected
```

### Rollback Procedures

- Always test the `down.sql` in staging before deploying `up.sql` to production
- Keep rollback window short — if the contract step has run, rollback requires a new forward migration
- For irreversible changes (dropping columns with data), take a logical backup first

---

## Performance Optimization

### Indexing Strategies

| Index Type | Use Case | Example |
|------------|----------|---------|
| **B-tree** (default) | Equality, range, ORDER BY | `CREATE INDEX idx_users_email ON users(email);` |
| **GIN** | Full-text search, JSONB, arrays | `CREATE INDEX idx_docs_body ON docs USING gin(to_tsvector('english', body));` |
| **GiST** | Geometry, range types, nearest-neighbor | `CREATE INDEX idx_locations ON places USING gist(coords);` |
| **Partial** | Subset of rows (reduce size) | `CREATE INDEX idx_active ON users(email) WHERE active = true;` |
| **Covering** | Index-only scans | `CREATE INDEX idx_cov ON orders(customer_id) INCLUDE (total, created_at);` |

### EXPLAIN Plan Reading

```sql
EXPLAIN (ANALYZE, BUFFERS, FORMAT TEXT) SELECT ...;
```

Key signals to watch:
- **Seq Scan** on large tables — missing index
- **Nested Loop** with high row estimates — consider hash/merge join or add index
- **Buffers shared read** much higher than **hit** — working set exceeds memory

### N+1 Query Detection

Symptoms: application issues one query per row (e.g., fetching related records in a loop).

Fixes:
- Use `JOIN` or subquery to fetch in one round-trip
- ORM eager loading (`select_related` / `includes` / `with`)
- DataLoader pattern for GraphQL resolvers

### Connection Pooling

| Tool | Protocol | Best For |
|------|----------|----------|
| **PgBouncer** | PostgreSQL | Transaction/statement pooling, low overhead |
| **ProxySQL** | MySQL | Query routing, read/write splitting |
| **Built-in pool** (HikariCP, SQLAlchemy pool) | Any | Application-level pooling |

**Rule of thumb:** Set pool size to `(2 * CPU cores) + disk spindles`. For cloud SSDs, start with `2 * vCPUs` and tune.

### Read Replicas and Query Routing

- Route all `SELECT` queries to replicas; writes to primary
- Account for replication lag (typically <1s for async, 0 for sync)
- Use `pg_last_wal_replay_lsn()` to detect lag before reading critical data

---

## Row-Level Security (RLS) Policies

Enforce multi-tenancy at the database layer. The application sets a session variable; policies read it.

```sql
ALTER TABLE tasks ENABLE ROW LEVEL SECURITY;
ALTER TABLE projects ENABLE ROW LEVEL SECURITY;

CREATE ROLE app_user;

-- Users can only see tasks in their organization's projects
CREATE POLICY tasks_org_isolation ON tasks
  FOR ALL TO app_user
  USING (
    project_id IN (
      SELECT p.id FROM projects p
      JOIN organization_members om ON om.organization_id = p.organization_id
      WHERE om.user_id = current_setting('app.current_user_id')::text
    )
  );

-- Soft delete: never show deleted records
CREATE POLICY tasks_no_deleted ON tasks
  FOR SELECT TO app_user
  USING (deleted_at IS NULL);

-- Only task creator or admin can delete
CREATE POLICY tasks_delete_policy ON tasks
  FOR DELETE TO app_user
  USING (
    created_by_id = current_setting('app.current_user_id')::text
    OR EXISTS (
      SELECT 1 FROM organization_members om
      JOIN projects p ON p.organization_id = om.organization_id
      WHERE p.id = tasks.project_id
        AND om.user_id = current_setting('app.current_user_id')::text
        AND om.role IN ('owner', 'admin')
    )
  );

-- Set user context at the start of each request
SELECT set_config('app.current_user_id', $1, true);
```

Always test RLS with a non-superuser role — superusers bypass RLS by default.

---

## Seed Data Generation

Generate realistic test data with Faker. Keep seed scripts idempotent and safe to re-run.

```typescript
// db/seed.ts
import { faker } from '@faker-js/faker'
import { db } from './client'
import { organizations, users, projects, tasks } from './schema'
import { createId } from '@paralleldrive/cuid2'
import { hashPassword } from '../src/lib/auth'

async function seed() {
  const [org] = await db.insert(organizations).values({
    id: createId(),
    name: faker.company.name(),
    slug: 'acme',
    plan: 'growth',
  }).returning()

  const adminUser = await db.insert(users).values({
    id: createId(),
    email: 'admin@acme.com',
    name: faker.person.fullName(),
    passwordHash: await hashPassword('password123'),
  }).returning().then(r => r[0])

  const projectsData = Array.from({ length: 3 }, () => ({
    id: createId(),
    organizationId: org.id,
    ownerId: adminUser.id,
    name: faker.company.catchPhrase(),
    description: faker.lorem.paragraph(),
    status: 'active' as const,
  }))

  const createdProjects = await db.insert(projects).values(projectsData).returning()

  for (const project of createdProjects) {
    const tasksData = Array.from({ length: faker.number.int({ min: 5, max: 20 }) }, (_, i) => ({
      id: createId(),
      projectId: project.id,
      title: faker.hacker.phrase(),
      description: faker.lorem.sentences(2),
      status: faker.helpers.arrayElement(['todo', 'in_progress', 'done'] as const),
      priority: faker.helpers.arrayElement(['low', 'medium', 'high'] as const),
      position: i * 1000,
      createdById: adminUser.id,
      updatedById: adminUser.id,
    }))
    await db.insert(tasks).values(tasksData)
  }
}

seed().catch(console.error).finally(() => process.exit(0))
```

---

## Common Schema Pitfalls

- **Soft delete without index** — `WHERE deleted_at IS NULL` without a partial index = full scan on every read
- **Missing composite indexes** — `WHERE org_id = ? AND status = ?` needs `(org_id, status)`, not two single-column indexes
- **Mutable surrogate keys** — never use email or slug as PK; use UUID/CUID
- **NOT NULL without default on existing table** — adding requires a default or a multi-step migration plan
- **No optimistic locking** — concurrent updates silently overwrite each other; add a `version` column
- **RLS not tested** — superusers bypass RLS; always test with the actual application role

---

## Multi-Database Decision Matrix

| Criteria | PostgreSQL | MySQL | SQLite | SQL Server |
|----------|-----------|-------|--------|------------|
| **Best for** | Complex queries, JSONB, extensions | Web apps, read-heavy workloads | Embedded, dev/test, edge | Enterprise .NET stacks |
| **JSON support** | Excellent (JSONB + GIN) | Good (JSON type) | Minimal | Good (OPENJSON) |
| **Replication** | Streaming, logical | Group replication, InnoDB cluster | N/A | Always On AG |
| **Licensing** | Open source (PostgreSQL License) | Open source (GPL) / commercial | Public domain | Commercial |
| **Max practical size** | Multi-TB | Multi-TB | ~1 TB (single-writer) | Multi-TB |

**When to choose:**
- **PostgreSQL** — default choice for new projects; best extensibility and standards compliance
- **MySQL** — existing MySQL ecosystem; simple read-heavy web applications
- **SQLite** — mobile apps, CLI tools, unit test databases, IoT/edge
- **SQL Server** — mandated by enterprise policy; deep .NET/Azure integration

### NoSQL Considerations

| Database | Model | Use When |
|----------|-------|----------|
| **MongoDB** | Document | Schema flexibility, rapid prototyping, content management |
| **Redis** | Key-value / cache | Session store, rate limiting, leaderboards, pub/sub |
| **DynamoDB** | Wide-column | Serverless AWS apps, single-digit-ms latency at any scale |

> Use SQL as default. Reach for NoSQL only when the access pattern clearly benefits from it.

---

## Sharding & Replication

### Horizontal vs Vertical Partitioning

- **Vertical partitioning**: Split columns across tables (e.g., separate BLOB columns). Reduces I/O for narrow queries.
- **Horizontal partitioning (sharding)**: Split rows across databases/servers. Required when a single node cannot hold the dataset or handle the throughput.

### Sharding Strategies

| Strategy | How It Works | Pros | Cons |
|----------|-------------|------|------|
| **Hash** | `shard = hash(key) % N` | Even distribution | Resharding is expensive |
| **Range** | Shard by date or ID range | Simple, good for time-series | Hot spots on latest shard |
| **Geographic** | Shard by user region | Data locality, compliance | Cross-region queries are hard |

### Replication Patterns

| Pattern | Consistency | Latency | Use Case |
|---------|------------|---------|----------|
| **Synchronous** | Strong | Higher write latency | Financial transactions |
| **Asynchronous** | Eventual | Low write latency | Read-heavy web apps |
| **Semi-synchronous** | At-least-one replica confirmed | Moderate | Balance of safety and speed |

---

## Cross-References

- **`architecture/storage-and-modeling-patterns`** — the conceptual frame for *what* to model (Kimball star, Inmon 3NF, Data Vault, SCD types, lakehouse vs warehouse). Use that skill to choose a model, then this one to implement it.
- **sql-database-assistant** — query writing, optimization, and debugging for day-to-day SQL work
- **migration-architect** — large-scale migration planning across database engines or major schema overhauls
- **senior-backend** — application-layer patterns (connection pooling, ORM best practices)
- **senior-devops** — infrastructure provisioning for database clusters and replicas

---

## Conclusion

Effective database design requires balancing multiple competing concerns: performance, scalability, maintainability, and business requirements. This skill provides the tools and knowledge to make informed decisions throughout the database lifecycle, from initial schema design through production optimization and evolution.

The included tools automate common analysis and optimization tasks, while the comprehensive guides provide the theoretical foundation for making sound architectural decisions. Whether building a new system or optimizing an existing one, these resources provide expert-level guidance for creating robust, scalable database solutions.
