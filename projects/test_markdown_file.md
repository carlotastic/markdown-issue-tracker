---
assignee: carlo
date: 2026-02-13
estimate: 3
linear-id: c001cc1d-23a0-4489-a26f-8f3bb110a038
priority: High
status: open
tags:
- ui
- bug
title: Fix login button alignment
---

# Issue Description
The login button on the mobile view is currently overlapping with the password field. This prevents users on smaller screens from tapping "Submit."

## Steps to Reproduce
1. Open the app on an iPhone SE.
2. Navigate to the Login screen.
3. Observe the overlap.

## Proposed Solution
Add a `margin-top: 20px` to the button container in the mobile CSS media query.