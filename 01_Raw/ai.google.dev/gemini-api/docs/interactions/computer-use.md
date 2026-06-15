---
source_url: https://ai.google.dev/gemini-api/docs/interactions/computer-use?hl=hi
fetched_at: 2026-06-15T06:21:28.653488+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini की Deep Research की सुविधा](https://ai.google.dev/gemini-api/docs/deep-research?hl=hi) अब झलक के तौर पर उपलब्ध है. इसमें साथ मिलकर प्लान बनाने, विज़ुअलाइज़ेशन, एमसीपी के साथ काम करने की सुविधा वगैरह शामिल है.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# कंप्यूटर का इस्तेमाल

कंप्यूटर का इस्तेमाल करने की सुविधा की मदद से, ब्राउज़र कंट्रोल करने वाले ऐसे एजेंट बनाए जा सकते हैं जो टास्क को ऑटोमेट करते हैं और उनके साथ इंटरैक्ट करते हैं. स्क्रीनशॉट का इस्तेमाल करके, मॉडल कंप्यूटर की स्क्रीन को "देख" सकता है. साथ ही, माउस क्लिक और कीबोर्ड इनपुट जैसे यूज़र इंटरफ़ेस (यूआई) ऐक्शन जनरेट करके "कार्रवाई" कर सकता है. फ़ंक्शन कॉलिंग की तरह ही, आपको कंप्यूटर का इस्तेमाल करने की सुविधा से जुड़ी कार्रवाइयां पाने और उन्हें लागू करने के लिए, क्लाइंट-साइड ऐप्लिकेशन कोड लिखना होगा.

कंप्यूटर के इस्तेमाल की सुविधा की मदद से, ऐसे एजेंट बनाए जा सकते हैं जो:

- वेबसाइटों पर बार-बार डेटा डालने या फ़ॉर्म भरने की प्रोसेस को अपने-आप होने की सुविधा चालू करें.
- वेब ऐप्लिकेशन और उपयोगकर्ता फ़्लो की ऑटोमेटेड टेस्टिंग करना
- अलग-अलग वेबसाइटों पर रिसर्च करना. जैसे, खरीदारी करने से पहले ई-कॉमर्स साइटों से प्रॉडक्ट की जानकारी, कीमतें, और समीक्षाएं इकट्ठा करना

कंप्यूटर इस्तेमाल करने की सुविधा को टेस्ट करने का सबसे आसान तरीका, [रेफ़रंस इंप्लीमेंटेशन](https://github.com/google/computer-use-preview/) या [Browserbase का डेमो एनवायरमेंट](http://gemini.browserbase.com) है.

## कंप्यूटर के इस्तेमाल की सुविधा कैसे काम करती है

कंप्यूटर इस्तेमाल करने वाले मॉडल की मदद से, ब्राउज़र कंट्रोल करने वाला एजेंट बनाने के लिए, एजेंट लूप लागू करें. यह लूप ये काम करता है:

1. [**मॉडल को अनुरोध भेजना**](#send-request)

   - अपने एपीआई अनुरोध में, कंप्यूटर इस्तेमाल करने से जुड़ा टूल जोड़ें. साथ ही, चाहें तो उपयोगकर्ता की ओर से तय किए गए कस्टम फ़ंक्शन या हटाए गए फ़ंक्शन भी जोड़ें.
   - उपयोगकर्ता के अनुरोध के साथ, कंप्यूटर के इस्तेमाल से जुड़े मॉडल को प्रॉम्प्ट करें.
2. [**मॉडल से जवाब पाना**](#model-response)

   - कंप्यूटर इस्तेमाल करने से जुड़ा मॉडल, उपयोगकर्ता के अनुरोध और स्क्रीनशॉट का विश्लेषण करता है. इसके बाद, एक जवाब जनरेट करता है. इसमें यूज़र इंटरफ़ेस (यूआई) से जुड़ी कार्रवाई को दिखाने वाला `function_call` शामिल होता है. जैसे, "कोऑर्डिनेट (x,y) पर क्लिक करें" या "'text' टाइप करें". कंप्यूटर इस्तेमाल करने से जुड़े मॉडल के साथ काम करने वाली यूज़र इंटरफ़ेस (यूआई) से जुड़ी सभी कार्रवाइयों के बारे में जानने के लिए, [काम करने वाली कार्रवाइयां](#supported-actions) देखें.
   - एपीआई से मिले जवाब में, इंटरनल सुरक्षा सिस्टम से मिला `safety_decision` भी शामिल हो सकता है. यह सिस्टम, मॉडल की सुझाई गई कार्रवाई की जांच करता है. यह `safety_decision`, कार्रवाई को इस तरह से कैटगरी में बांटता है:
     - **सामान्य / अनुमति है:** इस कार्रवाई को सुरक्षित माना जाता है. ऐसा भी हो सकता है कि कोई `safety_decision` मौजूद न हो.
     - **पुष्टि करना ज़रूरी है (`require_confirmation`):** मॉडल ऐसी कार्रवाई करने वाला है
       जो जोखिम भरी हो सकती है (जैसे, "कुकी स्वीकार करें" बैनर पर क्लिक करना).
3. [**कार्रवाई को पूरा करना**](#execute-actions)

   - आपके क्लाइंट-साइड कोड को `function_call` और उससे जुड़ा कोई भी `safety_decision` मिलता है.
     - **सामान्य / अनुमति है:** अगर `safety_decision` का मतलब सामान्य / अनुमति है या कोई `safety_decision` मौजूद नहीं है, तो क्लाइंट-साइड कोड, टारगेट एनवायरमेंट (जैसे, वेब ब्राउज़र) में तय किए गए `function_call` को लागू कर सकता है.
     - **पुष्टि करना ज़रूरी है:** अगर `safety_decision` से पता चलता है कि पुष्टि करना ज़रूरी है, तो आपका ऐप्लिकेशन `function_call` को लागू करने से पहले, उपयोगकर्ता से पुष्टि करने के लिए कहेगा. अगर उपयोगकर्ता पुष्टि करता है, तो कार्रवाई पूरी करें. अगर उपयोगकर्ता अनुमति नहीं देता है, तो कार्रवाई न करें.
4. [**नए एनवायरमेंट की स्थिति कैप्चर करना**](#capture-state)

   - अगर कार्रवाई पूरी हो गई है, तो आपका क्लाइंट, जीयूआई और मौजूदा यूआरएल का नया स्क्रीनशॉट कैप्चर करता है. इसके बाद, इसे `function_result` के हिस्से के तौर पर, Computer Use मॉडल को वापस भेजता है.
   - अगर सुरक्षा सिस्टम ने किसी कार्रवाई को ब्लॉक कर दिया है या उपयोगकर्ता ने पुष्टि करने से मना कर दिया है, तो हो सकता है कि आपका ऐप्लिकेशन, मॉडल को अलग तरह का सुझाव/राय/शिकायत भेजे या बातचीत खत्म कर दे.

यह प्रोसेस, दूसरे चरण से फिर शुरू होती है. इसमें मॉडल, नए स्क्रीनशॉट और मौजूदा लक्ष्य का इस्तेमाल करके अगली कार्रवाई का सुझाव देता है.यह लूप तब तक जारी रहता है, जब तक टास्क पूरा नहीं हो जाता, कोई गड़बड़ी नहीं होती या प्रोसेस बंद नहीं हो जाती. जैसे, सुरक्षा से जुड़े "ब्लॉक" जवाब या उपयोगकर्ता के फ़ैसले की वजह से.

![कंप्यूटर के इस्तेमाल की खास जानकारी](https://ai.google.dev/static/gemini-api/docs/images/computer_use.png?hl=hi)

## कंप्यूटर के इस्तेमाल की सुविधा कैसे लागू करें

कंप्यूटर के इस्तेमाल से जुड़ी सुविधा का इस्तेमाल करके ऐप्लिकेशन बनाने से पहले, आपको ये सेट अप करने होंगे:

- **सुरक्षित एक्ज़ीक्यूशन एनवायरमेंट:** सुरक्षा की वजहों से, आपको कंप्यूटर इस्तेमाल करने वाले एजेंट को सुरक्षित और कंट्रोल किए गए एनवायरमेंट में चलाना चाहिए. जैसे, सैंडबॉक्स की गई वर्चुअल मशीन, कंटेनर या सीमित अनुमतियों वाली ब्राउज़र प्रोफ़ाइल.
- **क्लाइंट-साइड ऐक्शन हैंडलर:** आपको क्लाइंट-साइड लॉजिक लागू करना होगा, ताकि मॉडल से जनरेट किए गए ऐक्शन को लागू किया जा सके. साथ ही, हर ऐक्शन के बाद एनवायरमेंट के स्क्रीनशॉट कैप्चर किए जा सकें.

इस सेक्शन में दिए गए उदाहरणों में, ब्राउज़र को एक्ज़ीक्यूशन एनवायरमेंट के तौर पर और [Playwright](https://playwright.dev/) को क्लाइंट-साइड ऐक्शन हैंडलर के तौर पर इस्तेमाल किया गया है. इन सैंपल को चलाने के लिए, आपको ज़रूरी डिपेंडेंसी इंस्टॉल करनी होंगी. साथ ही, Playwright ब्राउज़र इंस्टेंस को शुरू करना होगा:

### 0. Playwright इंस्टॉल करना

```
pip install google-genai playwright
playwright install chromium
```

### 0. Playwright ब्राउज़र इंस्टेंस शुरू करना

```
from playwright.sync_api import sync_playwright

# 1. Configure screen dimensions for the target environment
SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 900

# 2. Start the Playwright browser
# In production, utilize a sandboxed environment.
playwright = sync_playwright().start()
# Set headless=False to see the actions performed on your screen
browser = playwright.chromium.launch(headless=False)

# 3. Create a context and page with the specified dimensions
context = browser.new_context(
    viewport={"width": SCREEN_WIDTH, "height": SCREEN_HEIGHT}
)
page = context.new_page()

# 4. Navigate to an initial page to start the task
page.goto("https://www.google.com")

# The 'page', 'SCREEN_WIDTH', and 'SCREEN_HEIGHT' variables
# will be used in the steps below.
```

Android एनवायरमेंट के लिए, एक्सटेंड करने का सैंपल कोड [उपयोगकर्ता की ओर से तय किए गए कस्टम फ़ंक्शन इस्तेमाल करना](#custom-functions) सेक्शन में शामिल है.

### 1. मॉडल को अनुरोध भेजना

अपने एपीआई अनुरोध में, कंप्यूटर का इस्तेमाल करने वाले टूल को जोड़ें. साथ ही, मॉडल को ऐसा प्रॉम्प्ट भेजें जिसमें उपयोगकर्ता का लक्ष्य शामिल हो. आपको कंप्यूटर का इस्तेमाल करने वाले टूल के साथ काम करने वाले किसी एक मॉडल का इस्तेमाल करना होगा. ऐसा न करने पर, आपको गड़बड़ी का मैसेज मिलेगा:

- `gemini-2.5-computer-use-preview-10-2025`
- `gemini-3-flash-preview`

इसके अलावा, ये पैरामीटर भी जोड़े जा सकते हैं:

- **छोड़ी गई कार्रवाइयां:** अगर आपको [यूज़र इंटरफ़ेस (यूआई) पर की जा सकने वाली कार्रवाइयों](#supported-actions) की सूची में से कुछ कार्रवाइयां मॉडल से नहीं करानी हैं, तो उन कार्रवाइयों को `excluded_predefined_functions` के तौर पर मार्क करें.
- **उपयोगकर्ता के तय किए गए फ़ंक्शन:** कंप्यूटर के इस्तेमाल से जुड़ी जानकारी देने वाले टूल के अलावा, आपके पास उपयोगकर्ता के तय किए गए कस्टम फ़ंक्शन शामिल करने का विकल्प होता है.

ध्यान दें कि अनुरोध करते समय, डिसप्ले साइज़ के बारे में बताना ज़रूरी नहीं है;
मॉडल, स्क्रीन की ऊंचाई और चौड़ाई के हिसाब से पिक्सेल कोऑर्डिनेट का अनुमान लगाता है.

### Python

```
from google import genai

client = genai.Client()

# Specify predefined functions to exclude (optional)
excluded_functions = ["drag_and_drop"]

interaction = client.interactions.create(
    model='gemini-2.5-computer-use-preview-10-2025',
    input="Search for highly rated smart fridges with touchscreen, 2 doors, around 25 cu ft, priced below 4000 dollars on Google Shopping. Create a bulleted list of the 3 cheapest options in the format of name, description, price in an easy-to-read layout.",
    tools=[
        {
            "type": "computer_use",
            "environment": "browser",
            "excluded_predefined_functions": excluded_functions
        }
    ]
)

print(interaction)
```

कस्टम फ़ंक्शन के उदाहरण के लिए, [कस्टम फ़ंक्शन इस्तेमाल करना](#custom-functions) लेख पढ़ें.

### 2. मॉडल से जवाब पाना

कंप्यूटर का इस्तेमाल करने की सुविधा चालू होने पर, मॉडल एक या उससे ज़्यादा `function_call` चरणों में जवाब देगा. ऐसा तब होगा, जब उसे लगेगा कि टास्क पूरा करने के लिए यूज़र इंटरफ़ेस (यूआई) से जुड़ी कार्रवाइयां ज़रूरी हैं. कंप्यूटर का इस्तेमाल करने की सुविधा, एक साथ कई फ़ंक्शन कॉल करने की सुविधा के साथ काम करती है. इसका मतलब है कि मॉडल, एक ही बार में कई कार्रवाइयां कर सकता है.

यहां मॉडल के जवाब का एक उदाहरण दिया गया है.

```
{
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "I will type the search query into the search bar. The search bar is in the center of the page."
        }
      ]
    },
    {
      "type": "function_call",
      "name": "type_text_at",
      "arguments": {
        "x": 371,
        "y": 470,
        "text": "highly rated smart fridges with touchscreen, 2 doors, around 25 cu ft, priced below 4000 dollars on Google Shopping",
        "press_enter": true
      }
    }
  ]
}
```

### 3. मिली हुई कार्रवाइयों को लागू करना

आपके ऐप्लिकेशन कोड को मॉडल के जवाब को पार्स करना होगा, कार्रवाइयां करनी होंगी, और नतीजे इकट्ठा करने होंगे.

यहां दिए गए उदाहरण कोड में, Computer Use मॉडल के जवाब से फ़ंक्शन कॉल निकाले गए हैं. साथ ही, उन्हें ऐसी कार्रवाइयों में बदला गया है जिन्हें Playwright की मदद से पूरा किया जा सकता है. मॉडल, इनपुट इमेज के डाइमेंशन के बावजूद, सामान्य किए गए कोऑर्डिनेट (0-999) आउटपुट करता है. इसलिए, अनुवाद के चरण में इन सामान्य किए गए कोऑर्डिनेट को वापस पिक्सल की असल वैल्यू में बदला जाता है.

कंप्यूटर इस्तेमाल करने वाले मॉडल के साथ इस्तेमाल करने के लिए, स्क्रीन का सुझाया गया साइज़ (1440, 900) है. यह मॉडल किसी भी रिज़ॉल्यूशन के साथ काम करेगा. हालांकि, इससे नतीजों की क्वालिटी पर असर पड़ सकता है.

ध्यान दें कि इस उदाहरण में, सिर्फ़ तीन सबसे सामान्य यूज़र इंटरफ़ेस (यूआई) कार्रवाइयों को लागू करने के बारे में बताया गया है: `open_web_browser`, `click_at`, और `type_text_at`. प्रोडक्शन के इस्तेमाल के उदाहरणों के लिए, आपको [कार्रवाइयों के साथ काम करने वाले यूज़र इंटरफ़ेस (यूआई) एलिमेंट](#supported-actions) की सूची में मौजूद अन्य सभी यूज़र इंटरफ़ेस (यूआई) कार्रवाइयों को लागू करना होगा. ऐसा तब तक करना होगा, जब तक कि उन्हें `excluded_predefined_functions` के तौर पर साफ़ तौर पर न जोड़ दिया जाए.

### Python

```
from typing import Any, List, Tuple
import time

def denormalize_x(x: int, screen_width: int) -> int:
    """Convert normalized x coordinate (0-1000) to actual pixel coordinate."""
    return int(x / 1000 * screen_width)

def denormalize_y(y: int, screen_height: int) -> int:
    """Convert normalized y coordinate (0-1000) to actual pixel coordinate."""
    return int(y / 1000 * screen_height)

def execute_function_calls(interaction, page, screen_width, screen_height):
    results = []
    function_calls = [
        step for step in interaction.steps if step.type == "function_call"
    ]

    for function_call in function_calls:
        action_result = {}
        fname = function_call.name
        args = function_call.arguments
        print(f"  -> Executing: {fname}")

        try:
            if fname == "open_web_browser":
                pass # Already open
            elif fname == "click_at":
                actual_x = denormalize_x(args["x"], screen_width)
                actual_y = denormalize_y(args["y"], screen_height)
                page.mouse.click(actual_x, actual_y)
            elif fname == "type_text_at":
                actual_x = denormalize_x(args["x"], screen_width)
                actual_y = denormalize_y(args["y"], screen_height)
                text = args["text"]
                press_enter = args.get("press_enter", False)

                page.mouse.click(actual_x, actual_y)
                # Simple clear (Command+A, Backspace for Mac)
                page.keyboard.press("Meta+A")
                page.keyboard.press("Backspace")
                page.keyboard.type(text)
                if press_enter:
                    page.keyboard.press("Enter")
            else:
                print(f"Warning: Unimplemented or custom function {fname}")

            # Wait for potential navigations/renders
            page.wait_for_load_state(timeout=5000)
            time.sleep(1)

        except Exception as e:
            print(f"Error executing {fname}: {e}")
            action_result = {"error": str(e)}

        results.append((fname, function_call.id, action_result))

    return results
```

### 4. नए एनवायरमेंट की स्थिति कैप्चर करना

कार्रवाइयां पूरी होने के बाद, फ़ंक्शन के नतीजे को मॉडल को वापस भेजें, ताकि वह इस जानकारी का इस्तेमाल करके अगली कार्रवाई जनरेट कर सके. अगर एक साथ कई कार्रवाइयां (पैरलल कॉल) की गई हैं, तो आपको उपयोगकर्ता के अगले टर्न में हर कार्रवाई के लिए `function_result` भेजना होगा.

### Python

```
import json
import base64

def get_function_responses(page, results):
    screenshot_bytes = page.screenshot(type="png")
    current_url = page.url
    function_responses = []
    for name, call_id, result in results:
        function_responses.append({
            "type": "function_result",
            "name": name,
            "call_id": call_id,
            "result": [
                {
                    "type": "text",
                    "text": json.dumps({"url": current_url, **result})
                },
                {
                    "type": "image",
                    "data": base64.b64encode(screenshot_bytes).decode("utf-8"),
                    "mime_type": "image/png"
                }
            ]
        })
    return function_responses
```

## एजेंट लूप बनाना

एक से ज़्यादा चरणों वाले इंटरैक्शन को चालू करने के लिए, [कंप्यूटर के इस्तेमाल को लागू करने का तरीका](#implement-computer-use) सेक्शन में दिए गए चार चरणों को एक लूप में जोड़ें.
बातचीत के इतिहास को सही तरीके से मैनेज करना न भूलें. इसके लिए, मॉडल के जवाब और फ़ंक्शन के जवाब, दोनों को जोड़ें.

इस कोड सैंपल को चलाने के लिए, आपको ये काम करने होंगे:

- [Playwright की ज़रूरी डिपेंडेंसी](#implement-computer-use) इंस्टॉल करें.
- [(3) मिले हुए ऐक्शन लागू करें](#execute-actions) और [(4) नए एनवायरमेंट की स्थिति कैप्चर करें](#capture-state) चरणों में दिए गए हेल्पर फ़ंक्शन तय करें.

### Python

```
import time
from typing import Any, List, Tuple
from playwright.sync_api import sync_playwright

from google import genai

client = genai.Client()

# Constants for screen dimensions
SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 900

# Setup Playwright
print("Initializing browser...")
playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False)
context = browser.new_context(viewport={"width": SCREEN_WIDTH, "height": SCREEN_HEIGHT})
page = context.new_page()

# Define helper functions. Copy/paste from steps 3 and 4
# def denormalize_x(...)
# def denormalize_y(...)
# def execute_function_calls(...)
# def get_function_responses(...)

try:
    # Go to initial page
    page.goto("https://ai.google.dev/gemini-api/docs")

    # Take initial screenshot
    initial_screenshot = page.screenshot(type="png")
    USER_PROMPT = "Go to ai.google.dev/gemini-api/docs and search for pricing."
    print(f"Goal: {USER_PROMPT}")

    # First interaction
    interaction = client.interactions.create(
        model='gemini-2.5-computer-use-preview-10-2025',
        input=[
            {"type": "text", "text": USER_PROMPT},
            {"type": "image", "data": base64.b64encode(initial_screenshot).decode("utf-8"), "mime_type": "image/png"}
        ],
        tools=[{
            "type": "computer_use",
            "environment": "browser"
        }]
    )

    # Agent Loop
    turn_limit = 5
    for i in range(turn_limit):
        print(f"\n--- Turn {i+1} ---")

        has_function_calls = any(
            step.type == "function_call"
            for step in interaction.steps
        )
        if not has_function_calls:
            text_response = " ".join([
                content_block.text for step in interaction.steps if step.type == "model_output"
                for content_block in step.content if content_block.type == "text"
            ])
            print("Agent finished:", text_response)
            break

        print("Executing actions...")
        results = execute_function_calls(interaction, page, SCREEN_WIDTH, SCREEN_HEIGHT)

        print("Capturing state...")
        function_responses = get_function_responses(page, results)

        # Continue conversation with function responses
        interaction = client.interactions.create(
            model='gemini-2.5-computer-use-preview-10-2025',
            previous_interaction_id=interaction.id,
            input=function_responses,
            tools=[{
                "type": "computer_use",
                "environment": "browser"
            }]
        )

finally:
    # Cleanup
    print("\nClosing browser...")
    browser.close()
    playwright.stop()
```

## उपयोगकर्ता के तय किए गए कस्टम फ़ंक्शन का इस्तेमाल करना

मॉडल की सुविधाओं को बढ़ाने के लिए, अपने अनुरोध में उपयोगकर्ता के तय किए गए कस्टम फ़ंक्शन शामिल किए जा सकते हैं. हालांकि, ऐसा करना ज़रूरी नहीं है. यहाँ दिए गए उदाहरण में, कंप्यूटर के इस्तेमाल से जुड़े मॉडल और टूल को मोबाइल के इस्तेमाल के उदाहरणों के हिसाब से बनाया गया है. इसमें उपयोगकर्ता की ओर से तय की गई कस्टम कार्रवाइयाँ शामिल की गई हैं. जैसे, `open_app`, `long_press_at`, और `go_home`. वहीं, ब्राउज़र के हिसाब से की जाने वाली कार्रवाइयों को शामिल नहीं किया गया है. यह मॉडल, ब्राउज़र के बाहर के एनवायरमेंट में टास्क पूरे करने के लिए, स्टैंडर्ड यूज़र इंटरफ़ेस (यूआई) कार्रवाइयों के साथ-साथ इन कस्टम फ़ंक्शन को भी कॉल कर सकता है.

### Python

```
from typing import Optional, Dict, Any

from google import genai

client = genai.Client()

SYSTEM_PROMPT = """You are operating an Android phone. Today's date is October 15, 2023, so ignore any other date provided.
* To provide an answer to the user, *do not use any tools* and output your answer on a separate line. IMPORTANT: Do not add any formatting or additional punctuation/text, just output the answer by itself after two empty lines.
* Make sure you scroll down to see everything before deciding something isn't available.
* You can open an app from anywhere. The icon doesn't have to currently be on screen.
* Unless explicitly told otherwise, make sure to save any changes you make.
* If text is cut off or incomplete, scroll or click into the element to get the full text before providing an answer.
* IMPORTANT: Complete the given task EXACTLY as stated. DO NOT make any assumptions that completing a similar task is correct.  If you can't find what you're looking for, SCROLL to find it.
* If you want to edit some text, ONLY USE THE `type` tool. Do not use the onscreen keyboard.
* Quick settings shouldn't be used to change settings. Use the Settings app instead.
* The given task may already be completed. If so, there is no need to do anything.
"""

# Custom function definitions for mobile
custom_functions = [
    {
        "type": "function",
        "name": "open_app",
        "description": "Opens an app by name.",
        "parameters": {
            "type": "object",
            "properties": {
                "app_name": {"type": "string", "description": "Name of the app to open"},
                "intent": {"type": "string", "description": "Optional deep-link or action"}
            },
            "required": ["app_name"]
        }
    },
    {
        "type": "function",
        "name": "long_press_at",
        "description": "Long-press at a specific screen coordinate.",
        "parameters": {
            "type": "object",
            "properties": {
                "x": {"type": "integer", "description": "X coordinate"},
                "y": {"type": "integer", "description": "Y coordinate"}
            },
            "required": ["x", "y"]
        }
    },
    {
        "type": "function",
        "name": "go_home",
        "description": "Navigates to the device home screen.",
        "parameters": {"type": "object", "properties": {}}
    }
]

# Exclude browser-specific functions
excluded_functions = [
    "open_web_browser",
    "search",
    "navigate",
    "hover_at",
    "scroll_document",
    "go_forward",
    "key_combination",
    "drag_and_drop",
]

interaction = client.interactions.create(
    model='gemini-2.5-computer-use-preview-10-2025',
    system_instruction=SYSTEM_PROMPT,
    input="Open Chrome, then long-press at 200,400.",
    tools=[
        {
            "type": "computer_use",
            "environment": "browser",
            "excluded_predefined_functions": excluded_functions
        },
        *custom_functions
    ]
)

print(interaction)
```

## यूज़र इंटरफ़ेस (यूआई) पर की जा सकने वाली कार्रवाइयां

मॉडल, `function_call` का इस्तेमाल करके, यूज़र इंटरफ़ेस (यूआई) से जुड़ी इन कार्रवाइयों का अनुरोध कर सकता है. आपके क्लाइंट-साइड कोड को इन कार्रवाइयों के लिए, एक्ज़ीक्यूशन लॉजिक लागू करना होगा. उदाहरणों के लिए, [रेफ़रंस
इंपलीमेंटेशन](https://github.com/google/computer-use-preview) देखें.

| कमांड का नाम | ब्यौरा | आर्ग्युमेंट (फ़ंक्शन कॉल में) | फ़ंक्शन कॉल का उदाहरण |
| --- | --- | --- | --- |
| **open\_web\_browser** | इससे वेब ब्राउज़र खुलता है. | कोई नहीं | `{"name": "open_web_browser", "arguments": {}}` |
| **wait\_5\_seconds** | यह कुकी, पांच सेकंड के लिए स्क्रिप्ट को रोक देती है, ताकि डाइनैमिक कॉन्टेंट लोड हो सके या एनिमेशन पूरा हो सके. | कोई नहीं | `{"name": "wait_5_seconds", "arguments": {}}` |
| **go\_back** | यह कुकी, ब्राउज़र के इतिहास में पिछले पेज पर ले जाती है. | कोई नहीं | `{"name": "go_back", "arguments": {}}` |
| **go\_forward** | ब्राउज़र के इतिहास में अगले पेज पर ले जाता है. | कोई नहीं | `{"name": "go_forward", "arguments": {}}` |
| **search** | यह डिफ़ॉल्ट सर्च इंजन के होम पेज (जैसे, Google) पर जाता है. यह नई खोज शुरू करने के लिए काम का है. | कोई नहीं | `{"name": "search", "arguments": {}}` |
| **नेविगेट करें** | यह ब्राउज़र को सीधे तौर पर दिए गए यूआरएल पर ले जाता है. | `url`: str | `{"name": "navigate", "arguments": {"url": "https://www.wikipedia.org"}}` |
| **click\_at** | वेब पेज पर किसी खास कोऑर्डिनेट पर हुए क्लिक. x और y वैल्यू, 1000x1000 ग्रिड पर आधारित होती हैं. इन्हें स्क्रीन के डाइमेंशन के हिसाब से स्केल किया जाता है. | `y`: int (0-999), `x`: int (0-999) | `{"name": "click_at", "arguments": {"y": 300, "x": 500}}` |
| **hover\_at** | यह वेबपेज पर किसी खास जगह पर माउस को घुमाता है. यह सब-मेन्यू दिखाने के लिए काम आता है. x और y, 1000x1000 ग्रिड पर आधारित होते हैं. | `y`: int (0-999) `x`: int (0-999) | `{"name": "hover_at", "arguments": {"y": 150, "x": 250}}` |
| **type\_text\_at** | यह कमांड, किसी खास कोऑर्डिनेट पर टेक्स्ट टाइप करती है. डिफ़ॉल्ट रूप से, यह कमांड पहले फ़ील्ड को मिटाती है और फिर टाइप करने के बाद ENTER दबाती है. हालांकि, इन कार्रवाइयों को बंद किया जा सकता है. x और y, 1000x1000 ग्रिड पर आधारित होते हैं. | `y`: int (0-999), `x`: int (0-999), `text`: str, `press_enter`: bool (ज़रूरी नहीं, डिफ़ॉल्ट रूप से True पर सेट है), `clear_before_typing`: bool (ज़रूरी नहीं, डिफ़ॉल्ट रूप से True पर सेट है) | `{"name": "type_text_at", "arguments": {"y": 250, "x": 400, "text": "search query", "press_enter": false}}` |
| **key\_combination** | कीबोर्ड के बटन या उनके कॉम्बिनेशन दबाएं. जैसे, "Control+C" या "Enter". कार्रवाइयों को ट्रिगर करने (जैसे, "Enter" दबाकर फ़ॉर्म सबमिट करना) या क्लिपबोर्ड की कार्रवाइयों के लिए उपयोगी है. | `keys`: str (e.g. 'enter', 'control+c'). | `{"name": "key_combination", "arguments": {"keys": "Control+A"}}` |
| **scroll\_document** | इससे पूरे वेबपेज को "ऊपर", "नीचे", "बाएं" या "दाएं" की ओर स्क्रोल किया जाता है. | `direction`: str ("up", "down", "left" या "right") | `{"name": "scroll_document", "arguments": {"direction": "down"}}` |
| **scroll\_at** | यह फ़ंक्शन, किसी एलिमेंट या जगह को तय की गई दिशा में, तय की गई दूरी तक स्क्रोल करता है. कोऑर्डिनेट और मैग्नीट्यूड (डिफ़ॉल्ट रूप से 800), 1000x1000 ग्रिड पर आधारित होते हैं. | `y`: int (0-999), `x`: int (0-999), `direction`: str ("up", "down", "left", "right"), `magnitude`: int (0-999, Optional, default 800) | `{"name": "scroll_at", "arguments": {"y": 500, "x": 500, "direction": "down", "magnitude": 400}}` |
| **drag\_and\_drop** | यह फ़ंक्शन, किसी एलिमेंट को शुरुआती कोऑर्डिनेट (x, y) से खींचकर, डेस्टिनेशन कोऑर्डिनेट (destination\_x, destination\_y) पर छोड़ता है. सभी कोऑर्डिनेट, 1000x1000 ग्रिड पर आधारित होते हैं. | `y`: int (0-999), `x`: int (0-999), `destination_y`: int (0-999), `destination_x`: int (0-999) | `{"name": "drag_and_drop", "arguments": {"y": 100, "x": 100, "destination_y": 500, "destination_x": 500}}` |

## सुरक्षा और बचाव

### सुरक्षा से जुड़े फ़ैसले को स्वीकार करना

कार्रवाई के आधार पर, मॉडल के जवाब में `safety_decision` भी शामिल हो सकता है. यह एक इंटरनल सुरक्षा सिस्टम से मिलता है. यह सिस्टम, मॉडल की सुझाई गई कार्रवाई की जांच करता है.

```
{
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "I have evaluated step 2. It seems Google detected unusual traffic and is asking me to verify I'm not a robot. I need to click the 'I'm not a robot' checkbox located near the top left (y=98, x=95)."
        }
      ]
    },
    {
      "type": "function_call",
      "name": "click_at",
      "arguments": {
        "x": 60,
        "y": 100,
        "safety_decision": {
          "explanation": "I have encountered a CAPTCHA challenge that requires interaction. I need you to complete the challenge by clicking the 'I'm not a robot' checkbox and any subsequent verification steps.",
          "decision": "require_confirmation"
        }
      }
    }
  ]
}
```

अगर `safety_decision` `require_confirmation` है, तो आपको कार्रवाई करने से पहले, उपयोगकर्ता से पुष्टि करने के लिए कहना होगा. [सेवा की शर्तों](https://ai.google.dev/gemini-api/terms?hl=hi) के मुताबिक, आपको यह अनुमति नहीं है कि आप पुष्टि करने के लिए, इंसान के तौर पर की गई कार्रवाई के अनुरोधों को अनदेखा करें.

इस कोड सैंपल में, कार्रवाई करने से पहले उपयोगकर्ता से पुष्टि करने के लिए कहा जाता है. अगर उपयोगकर्ता कार्रवाई की पुष्टि नहीं करता है, तो लूप बंद हो जाता है. अगर उपयोगकर्ता कार्रवाई की पुष्टि करता है, तो कार्रवाई पूरी हो जाती है और `safety_acknowledgement` फ़ील्ड को `True` के तौर पर मार्क कर दिया जाता है.

### Python

```
import termcolor

def get_safety_confirmation(safety_decision):
    """Prompt user for confirmation when safety check is triggered."""
    termcolor.cprint("Safety service requires explicit confirmation!", color="red")
    print(safety_decision["explanation"])

    decision = ""
    while decision.lower() not in ("y", "n", "ye", "yes", "no"):
        decision = input("Do you wish to proceed? [Y]es/[N]o\n")

    if decision.lower() in ("n", "no"):
        return "TERMINATE"
    return "CONTINUE"

def execute_function_calls(interaction, page, screen_width, screen_height):

    # ... Extract function calls from response ...

    for function_call in function_calls:
        extra_fr_fields = {}

        # Check for safety decision
        if 'safety_decision' in function_call.arguments:
            decision = get_safety_confirmation(function_call.arguments['safety_decision'])
            if decision == "TERMINATE":
                print("Terminating agent loop")
                break
            extra_fr_fields["safety_acknowledgement"] = True # Safety acknowledgement

        # ... Execute function call and append to results ...
```

अगर उपयोगकर्ता पुष्टि करता है, तो आपको अपने `function_result` में सुरक्षा से जुड़ी सहमति शामिल करनी होगी.

```
```python
function_responses.append({
    "type": "function_result",
    "name": name,
    "call_id": function_call.id,
    "result": [
        {
            "type": "text",
            "text": json.dumps({
                "url": current_url,
                "safety_acknowledgement": True,
                **extra_fr_fields
            })
        },
        {
            "type": "image",
            "data": base64.b64encode(screenshot_bytes).decode("utf-8"),
            "mime_type": "image/png"
        }
    ]
})
```
```

### सुरक्षा के सबसे सही तरीके

कंप्यूटर का इस्तेमाल एक नया टूल है. इससे नए जोखिम पैदा होते हैं. डेवलपर को इनके बारे में पता होना चाहिए:

- **भरोसेमंद न होने वाला कॉन्टेंट और धोखाधड़ी:** मॉडल, उपयोगकर्ता के लक्ष्य को पूरा करने की कोशिश करता है. इसलिए, वह स्क्रीन पर मौजूद जानकारी और निर्देशों के लिए, भरोसेमंद न होने वाले सोर्स पर भरोसा कर सकता है. उदाहरण के लिए, अगर उपयोगकर्ता का लक्ष्य Pixel फ़ोन खरीदना है और मॉडल को "सर्वे पूरा करने पर मुफ़्त में Pixel पाएं" वाला कोई घोटाला मिलता है, तो इस बात की कुछ संभावना है कि मॉडल सर्वे पूरा कर देगा.
- **कभी-कभी अनचाही कार्रवाइयां:** मॉडल, उपयोगकर्ता के लक्ष्य या वेबपेज के कॉन्टेंट की गलत व्याख्या कर सकता है. इससे वह गलत कार्रवाइयां कर सकता है. जैसे, गलत बटन पर क्लिक करना या गलत फ़ॉर्म भरना. इससे टास्क पूरे नहीं हो पाते या डेटा चोरी हो सकता है.
- **नीति का उल्लंघन:** एपीआई की क्षमताओं का इस्तेमाल, जान-बूझकर या अनजाने में ऐसी गतिविधियों के लिए किया जा सकता है जो Google की नीतियों का उल्लंघन करती हैं. जैसे, [जनरेटिव एआई के इस्तेमाल से जुड़ी पाबंदी की नीति](https://policies.google.com/terms/generative-ai/use-policy?hl=hi) और [Gemini API की सेवा की अतिरिक्त शर्तें](https://ai.google.dev/gemini-api/terms?hl=hi). इसमें ऐसी कार्रवाइयां शामिल हैं जो किसी सिस्टम की अखंडता में रुकावट डाल सकती हैं, सुरक्षा से समझौता कर सकती हैं, सुरक्षा उपायों को दरकिनार कर सकती हैं, चिकित्सा उपकरणों को कंट्रोल कर सकती हैं वगैरह.

इन जोखिमों से बचने के लिए, सुरक्षा से जुड़े ये उपाय और सबसे सही तरीके अपनाए जा सकते हैं:

1. **ह्यूमन-इन-द-लूप (एचआईटीएल):**

   - **उपयोगकर्ता से पुष्टि कराएं:** अगर सुरक्षा से जुड़ी प्रतिक्रिया में `require_confirmation` दिखता है, तो आपको कार्रवाई करने से पहले उपयोगकर्ता से पुष्टि करानी होगी. सैंपल कोड के लिए, [सुरक्षा से जुड़े फ़ैसले की पुष्टि करना](#safety-decisions) लेख पढ़ें.
   - **सुरक्षा से जुड़े कस्टम निर्देश देना:** उपयोगकर्ता की पुष्टि करने के लिए, पहले से मौजूद जांचों के अलावा डेवलपर के पास यह विकल्प होता है कि वे [सिस्टम के लिए कस्टम निर्देश](https://ai.google.dev/gemini-api/docs/text-generation?hl=hi#system-instructions) जोड़ें. इससे, वे अपनी सुरक्षा नीतियों को लागू कर सकते हैं. ऐसा इसलिए किया जाता है, ताकि मॉडल की कुछ कार्रवाइयों को ब्लॉक किया जा सके या मॉडल के कुछ ऐसे फ़ैसलों के लिए उपयोगकर्ता की पुष्टि ज़रूरी हो जिन्हें बदला नहीं जा सकता. मॉडल के साथ इंटरैक्ट करते समय, यहां सिस्टम के लिए कस्टम निर्देश का एक उदाहरण दिया गया है.

     **सुरक्षा से जुड़े निर्देशों का उदाहरण:**

     सिस्टम के निर्देश के तौर पर, सुरक्षा से जुड़े अपने नियम सेट करें:

     ```
     ## **RULE 1: Seek User Confirmation (USER_CONFIRMATION)**

     This is your first and most important check. If the next required action falls
     into any of the following categories, you MUST stop immediately, and seek the
     user's explicit permission.

     **Procedure for Seeking Confirmation:**  * **For Consequential Actions:**
     Perform all preparatory steps (e.g., navigating, filling out forms, typing a
     message). You will ask for confirmation **AFTER** all necessary information is
     entered on the screen, but **BEFORE** you perform the final, irreversible action
     (e.g., before clicking "Send", "Submit", "Confirm Purchase", "Share").  * **For
     Prohibited Actions:** If the action is strictly forbidden (e.g., accepting legal
     terms, solving a CAPTCHA), you must first inform the user about the required
     action and ask for their confirmation to proceed.

     **USER_CONFIRMATION Categories:**

     *   **Consent and Agreements:** You are FORBIDDEN from accepting, selecting, or
         agreeing to any of the following on the user's behalf. You must ask the
         user to confirm before performing these actions.
         *   Terms of Service
         *   Privacy Policies
         *   Cookie consent banners
         *   End User License Agreements (EULAs)
         *   Any other legally significant contracts or agreements.
     *   **Robot Detection:** You MUST NEVER attempt to solve or bypass the
         following. You must ask the user to confirm before performing these actions.
     *   CAPTCHAs (of any kind)
         *   Any other anti-robot or human-verification mechanisms, even if you are
             capable.
     *   **Financial Transactions:**
         *   Completing any purchase.
         *   Managing or moving money (e.g., transfers, payments).
         *   Purchasing regulated goods or participating in gambling.
     *   **Sending Communications:**
         *   Sending emails.
         *   Sending messages on any platform (e.g., social media, chat apps).
         *   Posting content on social media or forums.
     *   **Accessing or Modifying Sensitive Information:**
         *   Health, financial, or government records (e.g., medical history, tax
             forms, passport status).
         *   Revealing or modifying sensitive personal identifiers (e.g., SSN, bank
             account number, credit card number).
     *   **User Data Management:**
         *   Accessing, downloading, or saving files from the web.
         *   Sharing or sending files/data to any third party.
         *   Transferring user data between systems.
     *   **Browser Data Usage:**
         *   Accessing or managing Chrome browsing history, bookmarks, autofill data,
             or saved passwords.
     *   **Security and Identity:**
         *   Logging into any user account.
         *   Any action that involves misrepresentation or impersonation (e.g.,
             creating a fan account, posting as someone else).
     *   **Insurmountable Obstacles:** If you are technically unable to interact with
         a user interface element or are stuck in a loop you cannot resolve, ask the
         user to take over.
     ---

     ## **RULE 2: Default Behavior (ACTUATE)**

     If an action does **NOT** fall under the conditions for `USER_CONFIRMATION`,
     your default behavior is to **Actuate**.

     **Actuation Means:**  You MUST proactively perform all necessary steps to move
     the user's request forward. Continue to actuate until you either complete the
     non-consequential task or encounter a condition defined in Rule 1.

     *   **Example 1:** If asked to send money, you will navigate to the payment
         portal, enter the recipient's details, and enter the amount. You will then
         **STOP** as per Rule 1 and ask for confirmation before clicking the final
         "Send" button.
     *   **Example 2:** If asked to post a message, you will navigate to the site,
         open the post composition window, and write the full message. You will then
         **STOP** as per Rule 1 and ask for confirmation before clicking the final
         "Post" button.

         After the user has confirmed, remember to get the user's latest screen
         before continuing to perform actions.

     # Final Response Guidelines:
     Write final response to the user in the following cases:
     - User confirmation
     - When the task is complete or you have enough information to respond to the user
     ```
2. **सुरक्षित एक्ज़ीक्यूशन एनवायरमेंट:** अपने एजेंट को सुरक्षित, सैंडबॉक्स वाले एनवायरमेंट में चलाएं, ताकि उसके संभावित असर को कम किया जा सके. उदाहरण के लिए, सैंडबॉक्स वाली वर्चुअल मशीन (वीएम), कंटेनर (जैसे, Docker) या सीमित अनुमतियों वाली ब्राउज़र प्रोफ़ाइल.
3. **इनपुट सैनिटाइज़ेशन:** प्रॉम्प्ट में मौजूद, उपयोगकर्ता के जनरेट किए गए सभी टेक्स्ट को सैनिटाइज़ करें. इससे अनचाहे निर्देशों या प्रॉम्प्ट इंजेक्शन के जोखिम को कम किया जा सकता है. यह सुरक्षा की एक मददगार लेयर है. हालांकि, यह सुरक्षित एक्ज़ीक्यूशन एनवायरमेंट का विकल्प नहीं है.
4. **कॉन्टेंट से जुड़े दिशा-निर्देश:** दिशा-निर्देशों और [कॉन्टेंट की सुरक्षा से जुड़े एपीआई](https://ai.google.dev/gemma/docs/shieldgemma?hl=hi) का इस्तेमाल करके, इन चीज़ों का आकलन करें: उपयोगकर्ता के इनपुट, टूल के इनपुट और आउटपुट, एजेंट के जवाब की उपयुक्तता, प्रॉम्प्ट इंजेक्शन, और जेलब्रेक का पता लगाना.
5. **अनुमति वाली और बिना अनुमति वाली सूचियां:** फ़िल्टर करने के तरीकों को लागू करें, ताकि यह कंट्रोल किया जा सके कि मॉडल किन वेबसाइटों पर जा सकता है और क्या कर सकता है. प्रतिबंधित वेबसाइटों की बिना अनुमति वाली सूची से शुरुआत करना अच्छा विकल्प है. हालांकि, अनुमति वाली सूची को ज़्यादा पाबंदियों के साथ इस्तेमाल करना ज़्यादा सुरक्षित होता है.
6. **निगरानी और लॉगिंग:** डीबग करने, ऑडिट करने, और सुरक्षा से जुड़े मामलों पर कार्रवाई करने के लिए, लॉग की पूरी जानकारी बनाए रखें. आपके क्लाइंट को प्रॉम्प्ट, स्क्रीनशॉट, मॉडल की सुझाई गई कार्रवाइयां (function\_call), सुरक्षा से जुड़े जवाब, और क्लाइंट की ओर से की गई सभी कार्रवाइयों को लॉग करना चाहिए.
7. **एनवायरमेंट मैनेजमेंट:** पक्का करें कि जीयूआई एनवायरमेंट एक जैसा हो.
   अचानक दिखने वाले पॉप-अप, सूचनाएं या लेआउट में होने वाले बदलावों से मॉडल को समझने में मुश्किल हो सकती है. अगर हो सके, तो हर नए काम के लिए, जानी-पहचानी और साफ़-सुथरी स्थिति से शुरुआत करें.

## मॉडल के वर्शन

ध्यान दें कि `gemini-3-flash-preview` में कंप्यूटर के इस्तेमाल की सुविधा पहले से मौजूद है. इस टूल को ऐक्सेस करने के लिए, आपको किसी अलग मॉडल की ज़रूरत नहीं है.

| प्रॉपर्टी | ब्यौरा |
| --- | --- |
| id\_cardमॉडल कोड | **Gemini API**  `gemini-2.5-computer-use-preview-10-2025` |
| saveइस्तेमाल किए जा सकने वाले डेटा टाइप | **इनपुट**  इमेज, टेक्स्ट  **आउटपुट**  टेक्स्ट |
| token\_autoटोकन की सीमाएं[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=hi) | **इनपुट टोकन की सीमा**  128,000  **आउटपुट टोकन की सीमा**  64,000 |
| 123वर्शन | ज़्यादा जानकारी के लिए, [मॉडल वर्शन के पैटर्न](https://ai.google.dev/gemini-api/docs/models/gemini?hl=hi#model-versions) पढ़ें.  - झलक देखें: `gemini-2.5-computer-use-preview-10-2025` |
| calendar\_monthनया अपडेट | अक्टूबर 2025 |

## आगे क्या करना है

- [Browserbase के डेमो एनवायरमेंट](http://gemini.browserbase.com) में, कंप्यूटर के इस्तेमाल से जुड़े एक्सपेरिमेंट करें.
- उदाहरण के लिए, कोड देखने के लिए [रेफ़रंस
  लागू करने का तरीका](https://github.com/google/computer-use-preview) देखें.
- Gemini API के अन्य टूल के बारे में जानें:
  - [फ़ंक्शन कॉलिंग](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=hi)
  - [Google Search से सटीक जानकारी पाने की सुविधा](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=hi)

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-06-05 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-06-05 (UTC) को अपडेट किया गया."],[],[]]
