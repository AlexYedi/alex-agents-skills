---
description: A pre-commit review request should load alex:karpathy-coder.
tags: [trigger, engineering]
max_turns: 8
allowed_tools: [Read, Glob, Grep, Skill]
---

Before I commit, karpathy check this diff. Am I overcomplicating it?

```python
-def total(items):
-    return sum(i.price for i in items)
+class PriceStrategy:
+    def apply(self, item): return item.price
+
+class Calculator:
+    def __init__(self, strategy=None):
+        self.strategy = strategy or PriceStrategy()
+    def total(self, items):
+        result = 0
+        for i in items:
+            result += self.strategy.apply(i)
+        return result
+
+def total(items):
+    return Calculator().total(items)
```
