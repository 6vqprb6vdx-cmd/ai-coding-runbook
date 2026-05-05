---
type: summary
source: 01_Raw/support.claude.com/en/articles/9020328-csam-detection-and-reporting.md
source_url: https://support.claude.com/en/articles/9020328-csam-detection-and-reporting
title: "Csam Detection and Reporting"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

Anthropic strictly prohibits Child Sexual Abuse Material (CSAM) on our services. We are committed to combatting CSAM distribution across our products and will report flagged media and related information to the National Center for Missing and Exploited Children (NCMEC).

As just one example of how we are combatting CSAM distribution: on our first-party services, we use a hash-matching tool to detect and report known CSAM that is included in a user or organization’s inputs. This tool provides access to NCMEC’s database of known CSAM hash values. When an image is sent in an input to our services, we will calculate a perceptual hash of the image. This hash will be automatically compared against the database. In the case of a match, we will notify and provide NCMEC information about the input and the related Account.
