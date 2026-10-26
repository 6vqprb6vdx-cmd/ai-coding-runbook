---
source_url: https://ai.google.dev/gemini-api/docs/coding-agents?hl=hi
fetched_at: 2026-10-26T05:57:48.667594+00:00
title: "\u0915\u094b\u0921\u093f\u0902\u0917 \u090f\u091c\u0947\u0902\u091f \u0938\u0947\u091f\u0905\u092a \u0915\u0930\u0928\u093e \u0914\u0930 \u0921\u0947\u0935\u0932\u092a\u0930 \u0915\u0947 \u0932\u093f\u090f \u0938\u0902\u0938\u093e\u0927\u0928 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon अब उपलब्ध है. [इसे आज़माएं](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=hi).

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# कोडिंग एजेंट सेटअप करना और डेवलपर के लिए संसाधन

एआई कोडिंग एजेंट, ट्रेनिंग डेटा पर निर्भर करते हैं. यह डेटा, एक तय तारीख तक का होता है. इस वजह से, एजेंट अक्सर ऐसे मॉडल (`gemini-1.5`), पुराने एसडीके (`google-generativeai`) या कोड पैटर्न का सुझाव देते हैं जो अब काम नहीं करते.

अपने एजेंट को Gemini के डेवलपर के लिए उपलब्ध आधिकारिक संसाधनों से कनेक्ट करने पर, उसे मौजूदा मॉडल, `google-genai` एसडीके, और [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) का इस्तेमाल करके सटीक कोड लिखने में मदद मिलती है.

कोडिंग एजेंट को Gemini के दस्तावेज़ और नियमों का ऐक्सेस इन चार तरीकों से दिया जा सकता है:

## एजेंट के संसाधनों के बारे में खास जानकारी

| संसाधन | इससे क्या मिलता है | उपलब्धता |
| --- | --- | --- |
| **[Gemini Agent की क्षमताएं](https://ai.google.dev/gemini-api/docs/coding-agents?hl=hi#available-skills)** | कुछ सुविधाओं (`gemini-api-dev`, `gemini-live-api-dev`, `gemini-omni-flash-api`) के लिए, चरण-दर-चरण दिए गए नियम, एसडीके पैटर्न, और हेल्पर स्क्रिप्ट. | [AI Studio Build](https://ai.studio/build) में पहले से इंस्टॉल है; `skills.sh`, Context7 या एजेंट बनाने और मैनेज करने की सुविधा की मदद से इंस्टॉल करें. |
| **[Gemini Docs MCP Server](https://ai.google.dev/gemini-api/docs/coding-agents?hl=hi#mcp-setup)** | सभी दस्तावेज़ों में, लाइव सर्च (`gemini_search_docs`) और पूरे पेज को पढ़ने की सुविधा (`gemini_get_doc`) उपलब्ध है. | यह सुविधा Claude Code, Cursor, OpenAI Codex, और VS Code में उपलब्ध है. |
| **[Gemini API प्लगिन](https://ai.google.dev/gemini-api/docs/coding-agents?hl=hi#gemini-api-plugin)** | यह बंडल किया गया पैकेज है. इसमें Gemini की आधिकारिक स्किल, Docs MCP सर्वर, और एपीआई पासकोड टूल शामिल हैं. | Antigravity. |
| **[मशीन से पढ़े जा सकने वाले दस्तावेज़](https://ai.google.dev/gemini-api/docs/coding-agents?hl=hi#machine-readable-docs)** | Markdown पेजों और `llms.txt` इंडेक्स को क्लीन करें. | `ai.google.dev/gemini-api/docs` पर मौजूद सभी दस्तावेज़ पेज. |

## Gemini एजेंट की स्किल इंस्टॉल करना

एजेंट की क्षमताओं से, कोडिंग एजेंट को प्रक्रिया से जुड़े नियम, मौजूदा मॉडल के नाम, और एसडीके के कोड पैटर्न मिलते हैं. अपने प्रॉम्प्ट में लंबे निर्देश जोड़ने के बजाय, आपका एजेंट हर स्किल को सिर्फ़ तब लोड करता है, जब उसकी ज़रूरत होती है. इससे आपके एजेंट को बंद किए गए SDK का इस्तेमाल करने से बचने और Gemini के नए पैटर्न का इस्तेमाल करने में मदद मिलती है.

स्किल, Gemini Docs के एमसीपी सर्वर के साथ काम करती हैं. अगर आपके एजेंट में एमसीपी सर्वर इंस्टॉल नहीं है, तो स्किल [`llms.txt`](https://ai.google.dev/gemini-api/docs/llms.txt?hl=hi) पर वापस आ जाती है. स्किल के काम करने के तरीके के बारे में ज़्यादा जानने के लिए, [Gemini API की स्किल गाइड](https://aistudio.google.com/learn/gemini-api-skills?hl=hi) पढ़ें.

### सीएलआई (`skills.sh` या Context7) की मदद से इंस्टॉल करना

[skills.sh](https://skills.sh) (सुझाया गया) या [Context7](https://context7.com) का इस्तेमाल करके, स्किल इंस्टॉल करें:

```
# List all available skills in the repository
npx skills add google-gemini/gemini-skills --list

# Install a specific skill globally with skills.sh
npx skills add google-gemini/gemini-skills --skill <skill-name> --global

# Or install with Context7
npx ctx7 skills install /google-gemini/gemini-skills <skill-name>
```

### उपलब्ध स्किल

#### `gemini-api-dev`

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) और Gemini API के आधिकारिक एसडीके (Python के लिए `google-genai` और TypeScript के लिए `@google/genai`) की मदद से ऐप्लिकेशन बनाने की स्किल. इस स्किल में ये विषय शामिल हैं:

- टेक्स्ट जनरेट करना, सिलसिलेवार बातचीत, स्ट्रीमिंग, स्ट्रक्चर्ड आउटपुट, और फ़ंक्शन कॉल करना
- इमेज जनरेट करने, लिखाई को बोली में बदलने (टीटीएस), और मल्टीमॉडल इनपुट की सुविधा
- सर्वर-साइड पर बातचीत की स्थिति को मैनेज करना, बैकग्राउंड में कोड एक्ज़ीक्यूट होना, डीप रिसर्च, और मैनेज किए गए एजेंट
- मौजूदा मॉडल के नाम और लेगसी `generateContent` या `google-generativeai` कोड माइग्रेट करना

```
npx skills add google-gemini/gemini-skills --skill gemini-api-dev --global
```

#### `gemini-live-api-dev`

[Gemini Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=hi) का इस्तेमाल करके, रीयल-टाइम में ऑडियो और वीडियो स्ट्रीमिंग ऐप्लिकेशन बनाने की स्किल. इस स्किल में ये विषय शामिल हैं:

- WebSocket सेशन मैनेजमेंट, कुछ समय के लिए उपलब्ध क्लाइंट टोकन, और सेशन फिर से शुरू करने की सुविधा
- आवाज़ का पता लगाने की तकनीक (वीएडी) और बार्ज-इन की सुविधा के साथ, ऑडियो, वीडियो, और टेक्स्ट स्ट्रीम करना
- बैकग्राउंड में गहराई से विश्लेषण (ज़्यादा समय लेकर सोचना), टूल को एसिंक्रोनस तरीके से कॉल करना, बोले जा रहे शब्दों को टेक्स्ट में बदलना, और Live बातचीत का अनुवाद करना

```
npx skills add google-gemini/gemini-skills --skill gemini-live-api-dev --global
```

#### `gemini-omni-flash-api`

इस स्किल की मदद से, Interactions API का इस्तेमाल करके Gemini Omni Flash से वीडियो जनरेट किए जा सकते हैं और उनमें बदलाव किया जा सकता है. इसमें हेल्पर स्क्रिप्ट (`upload_file.py`,
`generate_video.py`, `prep_video.py`, `inspect_video.py`) शामिल हैं. साथ ही, इसमें ये शामिल हैं:

- टेक्स्ट से वीडियो जनरेट करने और प्रॉम्प्ट बनाने की सुविधा
- पहले और आखिरी फ़्रेम के बीच ट्रांज़िशन और रेफ़रंस के हिसाब से वीडियो जनरेट करने की सुविधा
- वीडियो ऐसेट और मीडिया प्रीप्रोसेसिंग वर्कफ़्लो

```
npx skills add google-gemini/gemini-skills --skill gemini-omni-flash-api --global
```

### एजेंट बनाने और मैनेज करने की सुविधा में स्किल माउंट करना

Interactions API की मदद से रिमोट मैनेज किए गए एजेंट चलाने पर, `google-gemini/gemini-skills` रिपॉज़िटरी को एजेंट के वर्कस्पेस में माउंट किया जा सकता है. ज़्यादा जानकारी के लिए, [Gemini API की सुविधाओं से जुड़ी गाइड](https://aistudio.google.com/learn/gemini-api-skills?hl=hi) देखें:

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Build a script that generates a 5-second video of a neon cityscape.",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "repository",
                "source": "https://github.com/google-gemini/gemini-skills",
                "target": ".agents",
            }
        ],
    },
)
```

## Gemini Docs के एमसीपी सर्वर को कनेक्ट करना

सार्वजनिक **Gemini Docs MCP सर्वर** (`https://gemini-api-docs-mcp.dev`) की मदद से, आपका एजेंट पूरी दस्तावेज़ साइट को लाइव ऐक्सेस कर सकता है. आपका एजेंट, दस्तावेज़ के पेजों को खोज सकता है और उन्हें पढ़ सकता है. इससे वह अनुरोध के स्कीमा, मॉडल की सीमाओं, और नई सुविधाओं के बारे में जान सकता है:

- `gemini_search_docs`: यह सुविधा, विषय या क्वेरी के हिसाब से Gemini API के दस्तावेज़ खोजती है.
- `gemini_get_doc`: यह किसी दस्तावेज़ पेज के पूरे मार्कडाउन कॉन्टेंट को पढ़ता है.

### त्‍वरित सेटअप

पहचाने गए कोडिंग एजेंट को अपने-आप कॉन्फ़िगर करने के लिए, इस कमांड को अपने टर्मिनल या प्रोजेक्ट रूट में चलाएं:

```
npx add-mcp "https://gemini-api-docs-mcp.dev"
```

### एनवायरमेंट के हिसाब से कॉन्फ़िगरेशन

### Claude Code

अपने टर्मिनल में यह कमांड चलाएं:

```
$ claude mcp add --transport http geminiDocs https://gemini-api-docs-mcp.dev
```

### कर्सर

`~/.cursor/mcp.json` (ग्लोबल) या `.cursor/mcp.json` (प्रोजेक्ट) में जोड़ें:

```
{
  "mcpServers": {
    "geminiDocs": {
      "url": "https://gemini-api-docs-mcp.dev"
    }
  }
}
```

### OpenAI Codex

अपने टर्मिनल में यह कमांड चलाएं:

```
$ codex mcp add geminiDocs --url https://gemini-api-docs-mcp.dev
```

इसके अलावा, `~/.codex/config.toml` में जोड़ें:

```
[mcp_servers.geminiDocs]
url = "https://gemini-api-docs-mcp.dev"
```

### VS Code (Copilot)

अपने फ़ाइल फ़ोल्डर में `.vscode/mcp.json` जोड़ें:

```
{
  "servers": {
    "geminiDocs": {
      "type": "http",
      "url": "https://gemini-api-docs-mcp.dev"
    }
  }
}
```

## Gemini API प्लगिन

अगर **Antigravity** का इस्तेमाल किया जाता है, तो **Gemini API प्लगिन** की मदद से, अपने वर्कस्पेस को सबसे तेज़ी से सेट अप किया जा सकता है. इसमें Gemini Docs MCP सर्वर, Gemini की सभी आधिकारिक सुविधाएं (`gemini-api-dev`, `gemini-live-api-dev`, `gemini-omni-flash-api`), और एपीआई पासकोड टूल एक साथ डाउनलोड किए जा सकते हैं.

- **Antigravity (यूज़र इंटरफ़ेस) में इंस्टॉल करें:** **सेटिंग > पसंद के मुताबिक बनाएं > Google के प्लग-इन की मदद से बनाएं** पर जाएं और **Gemini API** डाउनलोड करें.
- **सीएलआई की मदद से इंस्टॉल करना:**
  `bash
  agy plugin install https://github.com/google-gemini/gemini-skills`

## मशीन से पढ़े जा सकने वाले दस्तावेज़

स्टैंडर्ड वेब पेजों में एचटीएमएल टैग, नेविगेशन बार, और स्क्रिप्ट शामिल होती हैं. ये कॉन्टेक्स्ट विंडो की जगह घेरती हैं. `ai.google.dev` मशीन से पढ़े जा सकने वाले एंडपॉइंट उपलब्ध कराता है, ताकि एजेंट और स्क्रिप्ट सीधे तौर पर साफ़-सुथरा मार्कडाउन फ़ेच कर सकें:

- **`llms.txt` इंडेक्स**
  ([`https://ai.google.dev/gemini-api/docs/llms.txt`](https://ai.google.dev/gemini-api/docs/llms.txt?hl=hi)):
  इसमें Gemini API के सभी दस्तावेज़ पेजों की सूची दी गई है. साथ ही, हर पेज के लिंक भी दिए गए हैं.
- **सीधे मार्कडाउन यूआरएल (`.md.txt`)**: सेव किए गए प्रॉम्प्ट, `AGENTS.md` नियमों या ऑटोमेटेड स्क्रिप्ट के लिए, साफ़ मार्कडाउन सोर्स पाने के लिए, `ai.google.dev` पर मौजूद किसी भी दस्तावेज़ के यूआरएल में `.md.txt` जोड़ें. उदाहरण के लिए, [`https://ai.google.dev/gemini-api/docs/coding-agents.md.txt`](https://ai.google.dev/gemini-api/docs/coding-agents.md.txt?hl=hi).

## प्रोजेक्ट के लिए सुझाए गए नियम (`AGENTS.md`)

प्रोजेक्ट की नियमों वाली फ़ाइल (`AGENTS.md`, `.cursorrules` या `CLAUDE.md`) में बुनियादी नियम सेट किए जाते हैं. ये नियम, हर एजेंट सेशन की शुरुआत में लोड होते हैं. इन दिशा-निर्देशों को अपने प्रोजेक्ट के रूट में जोड़ें, ताकि कोडिंग एजेंट डिफ़ॉल्ट रूप से मौजूदा मॉडल और एसडीके का इस्तेमाल कर सकें:

```
# Gemini API Guidelines

- Before writing Gemini API code, consult the `geminiDocs` MCP server (`gemini_search_docs` / `gemini_get_doc`) or `https://ai.google.dev/gemini-api/docs/llms.txt`.
- Always use the current Gemini API SDK (`google-genai` for Python, `@google/genai` for TypeScript/JavaScript). Never use legacy SDKs (`google-generativeai` or `@google/generative-ai`).
- Use the Interactions API (`client.interactions.create`) for new applications unless a specific feature requires `generateContent`.
- Use current recommended models (see https://ai.google.dev/gemini-api/docs/models) and avoid deprecated models.
```

## पुष्टि करना और समस्या हल करना

### अपने सेटअप की पुष्टि करें

अपने सेटअप की जांच करने के लिए, अपने कोडिंग एजेंट से ये सवाल पूछें:

```
Look up the request schema for the Gemini Interactions API in the documentation.
```

कॉन्फ़िगर किया गया एजेंट, `geminiDocs` एमसीपी सर्वर पर `gemini_search_docs` का इस्तेमाल करेगा. साथ ही, `google-genai` या `@google/genai` SDK टूल के साथ `client.interactions.create` का इस्तेमाल करके कोड लिखेगा.

### स्टेटस कमांड

| परिवेश | एमसीपी की पुष्टि | कौशल की पुष्टि करना |
| --- | --- | --- |
| **Claude Code** | रन `/mcp` | रन `/skills` |
| **कर्सर** | **सेटिंग > सुविधाएं > एमसीपी** खोलें | **सेटिंग > नियम** खोलें |
| **OpenAI Codex** | रन `codex mcp list` | `.codex/skills/` या `~/.codex/skills/` देखें |
| **Antigravity** | **पसंद के मुताबिक बनाएं > कनेक्शन** खोलें | **कस्टमाइज़ेशन > नियम** खोलें या `/skills list` चलाएं |
| **VS Code (Copilot)** | **एक्सटेंशन > एमसीपी** या आउटपुट पैनल खोलें | Copilot Chat में, **टूल चुनें** पर क्लिक करें |

### समस्या का हल

- **स्किल या एमसीपी सर्वर का पता नहीं चला:** अपने एडिटर (Cursor या VS Code) या टर्मिनल सेशन (Claude Code या Codex) को रीस्टार्ट करें. ज़्यादातर एजेंट, एमसीपी सर्वर और स्किल सिर्फ़ तब लोड करते हैं, जब वे शुरू होते हैं.
- **ग्लोबल स्किल का टकराव:** अगर आपका एजेंट, ग्लोबल तौर पर इंस्टॉल की गई किसी स्किल को अनदेखा करता है, तो `--global` के बिना अपने प्रोजेक्ट रूट में स्किल इंस्टॉल करें:
  `bash
  npx skills add google-gemini/gemini-skills --skill gemini-api-dev`
- **नियमों का पालन न करना:** पक्का करें कि आपकी `AGENTS.md`, `.cursorrules` या `CLAUDE.md` फ़ाइल, आपके प्रोजेक्ट की रूट डायरेक्ट्री में हो.

## आगे क्या करना है

- [Gemini API की क्षमताओं की गाइड](https://aistudio.google.com/learn/gemini-api-skills?hl=hi)
- [GitHub पर Gemini API की स्किल](https://github.com/google-gemini/gemini-skills)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi)
- [उपलब्ध मॉडल](https://ai.google.dev/gemini-api/docs/models?hl=hi)
- [लाइब्रेरी और एसडीके](https://ai.google.dev/gemini-api/docs/libraries?hl=hi)

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-10-06 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-10-06 (UTC) को अपडेट किया गया."],[],[]]
