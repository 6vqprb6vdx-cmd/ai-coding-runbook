---
source_url: https://support.claude.com/en/articles/12902446-claude-in-chrome-permissions-guide
fetched_at: 2026-05-04T16:55:15.433542+00:00
fetch_method: mintlify_md
---

Claude in Chrome is available in beta for all paid plans (Pro, Max, Team, and Enterprise) on the Chrome web browser.

This guide explains how to control what Claude can access and do when using Claude in Chrome. Understanding permissions helps you balance productivity with security.

**Important:** Before using Claude in Chrome, review [Using Claude in Chrome Safely](https://support.claude.com/en/articles/12902428-using-claude-for-chrome-safely) to understand the risks of browser-based AI.

## Permission Modes

Claude in Chrome uses a multi-layered permission system to give you control over what Claude can access and do. When you first open the extension, you'll see a drop-down menu on the chat input. Click this to choose between two permission modes:

- **Ask before acting:** Claude creates a plan and asks for approval before executing.

- **Act without asking:** Claude takes actions without asking for permission.

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1843322018/f8c0ae21b449f32e71696c76a17a/7656f295-e802-4a72-9e60-94611501f920?expires=1777915800&amp;signature=1ae30329ebbeb0056686b7e06b40e2180b93819d0cafcbaa5d8e9c1f7b8c54f6&amp;req=dSgjFcp8n4FeUfMW1HO4zQ5txiAF9H2%2FhD0gAzkS2hy1%2BBV2z4pbiERv4%2FLQ%0AzTXvAKkjBbEYjRbzMng%3D%0A)

---

## Ask before acting

Choose “Ask before acting” to have Claude create a plan from your prompt, which you can approve and allow Claude to execute. The plan will specify which websites you’re allowing Claude to access, as well as the approach it will follow:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1843320727/8d1c859ae9b8e0cdb536d024bf40/9bc3d239-8eb6-4bae-a032-a236f88ee606?expires=1777915800&amp;signature=bff88939bf10f46bc45cd855c21b391a52e704a60c53f85a9f4a2003db1a06d7&amp;req=dSgjFcp8nYZdXvMW1HO4zYqyasVE%2FYe%2FgN0ADj5oqFC46GXbrFXaDAVY7uuM%0AzFN1JbqVcI3Qk2KK188%3D%0A)

Note that Claude will only use the websites listed in the plan, so you’ll need to manually approve any additional access requests.

Claude clarifies which sites it’s planning to access and the actions it will take upfront, allowing you to review the proposed plan and ensure it’s correct before starting. You can also click “Make changes” to reject the current proposal, then prompt Claude again to make any necessary changes. Once you click “Approve plan,” Claude will be able to act independently within the outlined parameters, but will still check with you before taking certain irreversible actions, like making a purchase, creating an account, or downloading a file. Claude will not deviate from the stated plan without requesting your permission first. There are certain actions that Claude cannot take for your security, such as bypassing bot authorizations, executing trades, permanently deleting files, or taking certain actions that may indicate a prompt injection risk (see [Prohibited Actions](#h_e199f8f523)).

---

## Act without asking

"Act without asking" is a **high-risk mode** that allows Claude to operate with near-complete autonomy on the internet. Even in this mode, Claude should ask before:

- Making purchases or financial transactions

- Permanently deleting files or data

- Changing account passwords or security settings

However, due to the nature of LLMs, we can't guarantee that Claude will request permission to take these actions, so exercise caution when using this mode.

**Important:** Using "Act without asking" significantly increases prompt injection risk. Malicious actors may be able to trick Claude into unintended actions even with our safeguards.

Only allow Claude in Chrome to act without asking when:

- You're actively supervising Claude's actions.

- Working on trusted sites for routine tasks.

- You can immediately stop Claude if something seems wrong.

You remain fully responsible for all actions Claude takes when using this mode.

---

## When does Claude need to request additional permissions?

There are some websites on which Claude requires approval for every action. If you navigate to one of these sites, a **Permission required** prompt will appear in the extension side panel where Claude will ask for permission before accessing the page or taking any action.

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1847222875/162eb012ebe473ed2b852b97e223/0209db51-6057-4ec4-a9b7-8358287d46a3?expires=1777915800&amp;signature=ff01117e5335d27fb1bce5ade2c966cabda27dc13d99caa7ca2c188ae74a4b91&amp;req=dSgjEct8n4lYXPMW1HO4zeoCbMEionF3JCxYSFHKWIin461GPmJK2XrDT%2FDM%0AOjys2Xp2vE6GK4Wa3jk%3D%0A)

### Permission options

**"Allow this action"** grants permission for a single action only. Claude will ask again for the next action on this site. **This is the safest option when using the extension** as you can review and approve each of Claude's actions.

**"Always allow actions on this site"** grants ongoing permission for this website. Claude can take multiple actions without asking each time. Only use this for sites you completely trust. Claude may take unintended actions across the website when granted this permission.

**"Decline"** prevents Claude from taking this action. You can try a different approach or skip this task.

### Protected actions

When you choose "Always allow actions on this site," Claude still asks for your explicit approval before:

- Making purchases or financial transactions

- Permanently deleting files or data

- Modifying permissions settings

- Creating accounts

### Managing site permissions

You can manage Claude's access to specific sites in the extension settings. Click the Claude extension icon, then the three dots in the upper right corner of the side panel. Select "Settings" → "Permissions" to:

- Review which sites have "always allow" status under **Your approved sites**

- Revoke permissions for specific websites

- See your permission history

---

## Organization-level controls (Team and Enterprise plans)

Team and Enterprise admins can configure additional controls that affect permissions:

- **Allowlists** restrict Claude to only access approved sites

- **Blocklists** prevent Claude from accessing specific sites, regardless of user permissions

If you're unable to access a site with Claude, your organization may have restricted access. Contact your admin for more information, or see [Claude in Chrome Admin Controls](https://support.claude.com/en/articles/13065128-claude-for-chrome-admin-controls).

---

## Actions Requiring Explicit Permission

Regardless of your permission mode, Claude requires explicit user permission to perform any of the following actions:

- Making purchases or financial transactions

- Permanently deleting files or data

- Modifying permissions settings

- Creating accounts

- Granting authorizations

- Inputting potentially sensitive information into websites

---

## Prohibited Actions

To protect you, Claude is prohibited from taking following actions regardless of permissions:

- Handling sensitive credit card or ID data

- Downloading files from untrusted sources

- Permanent deletions (emptying trash, deleting emails, files, or messages)

- Modifying security permissions or access controls

- Providing investment or financial advice

- Executing financial trades or investment transactions

- Modifying system files

- Completing instructions from emails or web content
