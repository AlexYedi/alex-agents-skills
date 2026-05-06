# Provider Catalog

> **What this is:** A human-readable reference catalog of 150+ B2B data enrichment providers with their capabilities, credit costs, and success-rate estimates. The YAML below is reference notation for scannability — **it is not loaded by code**. Update by hand when adding/removing providers or revising costs.
>
> **What this is *not*:** Selection rules, waterfall sequences, or budget profiles. Those live in [`../skills/waterfall-blueprint/SKILL.md`](../skills/waterfall-blueprint/SKILL.md) — that's the design playbook for *how to compose* providers from this catalog.

**Last reviewed:** 2026-05-06
**Next review due:** 2026-08-06 (quarterly)

## Provider Capabilities

```yaml
providers:
  # ============================================
  # EMAIL & CONTACT DISCOVERY (25+ providers)
  # ============================================
  
  apollo_io:
    name: "Apollo.io"
    category: "email_contact"
    capabilities:
      - name: "Find Work Email"
        credits: [1, 2]
        success_rate: 75%
        inputs: ["name+company", "linkedin_url", "domain"]
      - name: "Find Personal Email"
        credits: [1, 2]
        success_rate: 60%
      - name: "Phone Number Lookup"
        credits: [1, 2]
        success_rate: 65%
      - name: "LinkedIn Profile URL"
        credits: 1
        success_rate: 85%
      - name: "Job Title Enrichment"
        credits: 1
        success_rate: 90%
      - name: "Company Information"
        credits: 1
        success_rate: 95%
      - name: "Contact Verification"
        credits: 0.5
        success_rate: 98%
      - name: "Technographics"
        credits: 2
        success_rate: 70%
    best_for: ["US B2B", "Sales teams", "LinkedIn data"]
    bulk_discounts:
      1000: 10%
      5000: 20%
      10000: 30%
    
  hunter:
    name: "Hunter"
    category: "email_discovery"
    capabilities:
      - name: "Domain Email Search"
        credits: 1
        success_rate: 80%
        inputs: ["domain"]
      - name: "Email Finder"
        credits: [1, 2]
        success_rate: 70%
        inputs: ["name+domain"]
      - name: "Email Verification"
        credits: 0.5
        success_rate: 95%
      - name: "Email Patterns"
        credits: 1
        success_rate: 90%
      - name: "Author Finder"
        credits: 1
        success_rate: 65%
    best_for: ["Domain searches", "Email patterns", "Content creators"]
    
  rocketreach:
    name: "RocketReach"
    category: "email_contact"
    capabilities:
      - name: "Email Discovery"
        credits: [1, 2]
        success_rate: 70%
      - name: "Phone Numbers"
        credits: [1, 2]
        success_rate: 60%
      - name: "Social Profiles"
        credits: 1
        success_rate: 75%
      - name: "Contact Verification"
        credits: 0.5
        success_rate: 95%
    best_for: ["Personal emails", "Professional contacts"]
    
  contactout:
    name: "ContactOut"
    category: "linkedin_enrichment"
    capabilities:
      - name: "LinkedIn Email Extraction"
        credits: [1, 2]
        success_rate: 80%
        inputs: ["linkedin_url"]
      - name: "Phone Number Finder"
        credits: [1, 2]
        success_rate: 65%
      - name: "Contact Verification"
        credits: 0.5
        success_rate: 95%
      - name: "Bulk Processing"
        credits: 1  # per contact
        success_rate: 75%
    best_for: ["LinkedIn profiles", "Chrome extension users"]
    
  findymail:
    name: "Findymail"
    category: "email_discovery"
    capabilities:
      - name: "Email Discovery"
        credits: [1, 2]
        success_rate: 75%
      - name: "Email Verification"
        credits: 0.5
        success_rate: 98%
      - name: "LinkedIn Integration"
        credits: 1
        success_rate: 80%
      - name: "Bulk Processing"
        credits: 1  # per email
        success_rate: 75%
    best_for: ["AI-powered finding", "High deliverability"]
    
  bettercontact:
    name: "BetterContact"
    category: "waterfall_enrichment"
    capabilities:
      - name: "Email Waterfall"
        credits: [2, 5]
        success_rate: 85%
        description: "Runs multiple providers sequentially"
      - name: "Phone Waterfall"
        credits: [2, 5]
        success_rate: 70%
      - name: "Contact Verification"
        credits: 0.5
        success_rate: 98%
      - name: "Data Enrichment"
        credits: [1, 3]
        success_rate: 80%
    best_for: ["Maximum success rates", "Hard-to-find contacts"]
    
  # ============================================
  # COMPANY INTELLIGENCE (20+ providers)
  # ============================================
  
  clearbit:
    name: "Clearbit"
    category: "company_intelligence"
    capabilities:
      - name: "Company Enrichment"
        credits: [1, 2]
        success_rate: 90%
        inputs: ["domain", "company_name"]
      - name: "Person Enrichment"
        credits: [1, 2]
        success_rate: 75%
        inputs: ["email"]
      - name: "Email Discovery"
        credits: [1, 2]
        success_rate: 70%
      - name: "Logo API"
        credits: 0.5
        success_rate: 95%
      - name: "Prospector"
        credits: [2, 3]
        success_rate: 80%
      - name: "Risk Assessment"
        credits: 1
        success_rate: 85%
    best_for: ["Company data", "Real-time enrichment", "API integration"]
    bulk_discounts:
      volume_tier: 25%
    
  zoominfo:
    name: "ZoomInfo"
    category: "enterprise_intelligence"
    capabilities:
      - name: "Contact Intelligence"
        credits: [2, 3]
        success_rate: 90%
      - name: "Company Intelligence"
        credits: [2, 3]
        success_rate: 95%
      - name: "Technographics"
        credits: [2, 3]
        success_rate: 85%
      - name: "Intent Data"
        credits: [3, 5]
        success_rate: 75%
      - name: "Org Charts"
        credits: [2, 3]
        success_rate: 80%
      - name: "Sales Intelligence"
        credits: [2, 4]
        success_rate: 85%
      - name: "Market Intelligence"
        credits: [3, 4]
        success_rate: 80%
      - name: "Lead Scoring"
        credits: [2, 3]
        success_rate: 85%
    best_for: ["Enterprise accounts", "Comprehensive data", "Intent signals"]
    bulk_discounts:
      enterprise_agreement: 40%
    
  crunchbase:
    name: "Crunchbase"
    category: "funding_intelligence"
    capabilities:
      - name: "Funding Information"
        credits: [1, 2]
        success_rate: 95%
      - name: "Company Financials"
        credits: [1, 2]
        success_rate: 85%
      - name: "Investor Data"
        credits: 1
        success_rate: 90%
      - name: "News and Updates"
        credits: 1
        success_rate: 95%
      - name: "Acquisition Data"
        credits: [1, 2]
        success_rate: 90%
    best_for: ["Startups", "Funding data", "Investor information"]
    
  pitchbook:
    name: "PitchBook"
    category: "private_market"
    capabilities:
      - name: "Private Market Data"
        credits: [3, 5]
        success_rate: 95%
      - name: "Funding Intelligence"
        credits: [2, 3]
        success_rate: 95%
      - name: "Investor Data"
        credits: [2, 3]
        success_rate: 90%
      - name: "M&A Intelligence"
        credits: [3, 4]
        success_rate: 90%
    best_for: ["Private equity", "Detailed financials", "M&A data"]
    
  # ============================================
  # TECHNOLOGY INTELLIGENCE (8+ providers)
  # ============================================
  
  builtwith:
    name: "BuiltWith"
    category: "technographics"
    capabilities:
      - name: "Technology Stack"
        credits: [1, 2]
        success_rate: 90%
        inputs: ["domain"]
      - name: "CMS Detection"
        credits: 1
        success_rate: 95%
      - name: "Analytics Tools"
        credits: 1
        success_rate: 90%
      - name: "Marketing Technology"
        credits: [1, 2]
        success_rate: 85%
      - name: "E-commerce Platform"
        credits: 1
        success_rate: 95%
      - name: "Historical Technology"
        credits: 2
        success_rate: 80%
    best_for: ["Tech stack", "E-commerce detection", "Historical data"]
    
  hg_insights:
    name: "HG Insights"
    category: "technology_intelligence"
    capabilities:
      - name: "Technology Intelligence"
        credits: [2, 3]
        success_rate: 85%
      - name: "Software Installations"
        credits: 2
        success_rate: 80%
      - name: "IT Spend Analysis"
        credits: [2, 3]
        success_rate: 75%
      - name: "Competitive Intelligence"
        credits: [2, 4]
        success_rate: 80%
    best_for: ["Enterprise tech", "IT spend", "Technology adoption"]
    
  # ============================================
  # AI & CONTENT GENERATION (15+ providers)
  # ============================================
  
  openai_gpt:
    name: "OpenAI/GPT"
    category: "ai_generation"
    capabilities:
      - name: "AI Content Generation"
        credits: [2, 5]
        success_rate: 95%
      - name: "Text Analysis"
        credits: [1, 3]
        success_rate: 95%
      - name: "Research Assistance"
        credits: [2, 4]
        success_rate: 90%
      - name: "Data Interpretation"
        credits: [1, 3]
        success_rate: 90%
    best_for: ["Content creation", "Analysis", "Custom tasks"]
    
  anthropic:
    name: "Anthropic"
    category: "ai_analysis"
    capabilities:
      - name: "AI Text Analysis"
        credits: [1, 3]
        success_rate: 95%
      - name: "Content Generation"
        credits: [2, 5]
        success_rate: 95%
      - name: "Data Interpretation"
        credits: [1, 2]
        success_rate: 95%
      - name: "Research Assistance"
        credits: [2, 4]
        success_rate: 90%
    best_for: ["Complex reasoning", "Long-form content", "Analysis"]
    
  # ============================================
  # VERIFICATION SERVICES (8+ providers)
  # ============================================
  
  zerobounce:
    name: "ZeroBounce"
    category: "email_verification"
    capabilities:
      - name: "Email Verification"
        credits: 0.5
        success_rate: 99%
      - name: "Spam Trap Detection"
        credits: 0.5
        success_rate: 95%
      - name: "Bounce Detection"
        credits: 0.5
        success_rate: 98%
      - name: "Email Scoring"
        credits: 0.5
        success_rate: 95%
      - name: "List Cleaning"
        credits: 0.5  # per email
        success_rate: 98%
      - name: "Deliverability Analysis"
        credits: 1
        success_rate: 90%
    best_for: ["Email validation", "List hygiene", "Deliverability"]
    
  neverbounce:
    name: "NeverBounce"
    category: "email_verification"
    capabilities:
      - name: "Email Verification"
        credits: 0.5
        success_rate: 98%
      - name: "List Cleaning"
        credits: 0.5  # per email
        success_rate: 97%
      - name: "Deliverability Analysis"
        credits: 0.5
        success_rate: 95%
      - name: "Real-time Validation"
        credits: 0.5
        success_rate: 99%
    best_for: ["Real-time validation", "Bulk cleaning"]
    
  # ============================================
  # SALES & CRM INTEGRATION (25+ providers)
  # ============================================
  
  salesforce:
    name: "Salesforce"
    category: "crm_integration"
    capabilities:
      - name: "CRM Integration"
        credits: 0
        success_rate: 100%
      - name: "Lead Management"
        credits: 0.5
        success_rate: 100%
      - name: "Account Data"
        credits: 0.5
        success_rate: 100%
      - name: "Pipeline Analytics"
        credits: 1
        success_rate: 95%
    best_for: ["CRM sync", "Lead management", "Enterprise"]
    
  hubspot:
    name: "HubSpot"
    category: "crm_marketing"
    capabilities:
      - name: "CRM Integration"
        credits: 0
        success_rate: 100%
      - name: "Contact Management"
        credits: 0.5
        success_rate: 100%
      - name: "Deal Tracking"
        credits: 1
        success_rate: 100%
      - name: "Marketing Automation"
        credits: 1
        success_rate: 95%
    best_for: ["Inbound marketing", "SMB CRM", "Automation"]
    
  gong:
    name: "Gong"
    category: "conversation_intelligence"
    capabilities:
      - name: "Sales Call Analysis"
        credits: [3, 5]
        success_rate: 90%
      - name: "Conversation Intelligence"
        credits: [3, 5]
        success_rate: 90%
      - name: "Performance Metrics"
        credits: [2, 3]
        success_rate: 95%
      - name: "Deal Intelligence"
        credits: [2, 4]
        success_rate: 85%
    best_for: ["Sales coaching", "Call analysis", "Deal insights"]
    
  # ============================================
  # SOCIAL MEDIA & CONTENT (15+ providers)
  # ============================================
  
  linkedin:
    name: "LinkedIn"
    category: "social_professional"
    capabilities:
      - name: "Profile Data"
        credits: [1, 2]
        success_rate: 95%
      - name: "Professional Networks"
        credits: 1
        success_rate: 90%
      - name: "Activity Tracking"
        credits: 1
        success_rate: 85%
      - name: "Company Affiliations"
        credits: 1
        success_rate: 95%
    best_for: ["Professional data", "B2B networking"]
    
  twitter_x:
    name: "X.com (Twitter)"
    category: "social_media"
    capabilities:
      - name: "Profile Intelligence"
        credits: [1, 2]
        success_rate: 90%
      - name: "Tweet Analysis"
        credits: 1
        success_rate: 95%
      - name: "Follower Analytics"
        credits: [1, 2]
        success_rate: 90%
      - name: "Social Listening"
        credits: [2, 3]
        success_rate: 85%
      - name: "Engagement Metrics"
        credits: 1
        success_rate: 95%
      - name: "Influence Scoring"
        credits: [1, 2]
        success_rate: 85%
    best_for: ["Social listening", "Influencer identification"]
    
  # ============================================
  # WEB SCRAPING & DATA EXTRACTION (10+ providers)
  # ============================================
  
  apify:
    name: "Apify"
    category: "web_scraping"
    capabilities:
      - name: "Web Scraping"
        credits: [1, 5]
        success_rate: 90%
      - name: "Social Media Scraping"
        credits: [2, 4]
        success_rate: 85%
      - name: "E-commerce Data"
        credits: [2, 3]
        success_rate: 90%
      - name: "Search Engine Results"
        credits: [1, 2]
        success_rate: 95%
      - name: "Directory Scraping"
        credits: [1, 3]
        success_rate: 90%
    best_for: ["Custom scraping", "Large-scale extraction"]
    
  phantombuster:
    name: "PhantomBuster"
    category: "social_automation"
    capabilities:
      - name: "Social Media Automation"
        credits: [2, 4]
        success_rate: 85%
      - name: "Data Extraction"
        credits: [2, 3]
        success_rate: 85%
      - name: "Lead Generation"
        credits: [2, 4]
        success_rate: 80%
      - name: "Profile Scraping"
        credits: [1, 3]
        success_rate: 85%
    best_for: ["LinkedIn automation", "Social scraping"]
    
  # ============================================
  # NATIVE CAPABILITIES (No external dependencies)
  # ============================================
  
  native_operations:
    name: "Native Operations"
    category: "internal"
    capabilities:
      - name: "Formula Fields"
        credits: 0
        success_rate: 100%
      - name: "Text Formatting"
        credits: 0
        success_rate: 100%
      - name: "Date Calculations"
        credits: 0
        success_rate: 100%
      - name: "Deduplication"
        credits: 0
        success_rate: 100%
      - name: "Field Mapping"
        credits: 0
        success_rate: 100%
      - name: "Data Validation"
        credits: 0
        success_rate: 100%
      - name: "Table Operations"
        credits: 0
        success_rate: 100%
      - name: "Workflow Automation"
        credits: 0
        success_rate: 100%
    best_for: ["Data processing", "Cost optimization", "Speed"]
```

## See Also

- [`../skills/waterfall-blueprint/SKILL.md`](../skills/waterfall-blueprint/SKILL.md) — provider selection rules per enrichment type, credit-budget profiles (Maximum Success / Balanced / Budget), and optimization tactics. *That* is where you go when designing a sequence; this catalog is where you go when looking up what a single provider does.
- [`../skills/waterfall-blueprint/references/provider_cheat_sheet.md`](../skills/waterfall-blueprint/references/provider_cheat_sheet.md) — the at-a-glance shortlist for in-context decisions.
- [`../skills/provider-scorecard/SKILL.md`](../skills/provider-scorecard/SKILL.md) — track observed performance against the success-rate estimates in this catalog and update them on the next quarterly review.

## Update Process

1. New provider, removed provider, or changed costs → edit this file directly.
2. Update the **Last reviewed** date at the top.
3. Note material changes in the bundle's git history (commit message is enough; no separate changelog needed at this scale).
4. Quarterly: run `provider-scorecard` over the last 90 days of usage and reconcile observed success rates against the estimates here.
