---
source_url: https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=vi
fetched_at: 2026-11-02T07:27:43.806117+00:00
title: "Chi\u1ebfn l\u01b0\u1ee3c thi\u1ebft k\u1ebf c\u00e2u l\u1ec7nh \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon hiện đã ra mắt. [Hãy dùng thử](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=vi).

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google sử dụng công nghệ AI để dịch nội dung sang ngôn ngữ bạn ưu tiên. Bản dịch bằng AI có thể có lỗi.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Chiến lược thiết kế câu lệnh

*Thiết kế câu lệnh* là quá trình tạo câu lệnh hoặc yêu cầu bằng ngôn ngữ tự nhiên, giúp mô hình ngôn ngữ đưa ra câu trả lời chính xác và chất lượng cao.

Trang này giới thiệu các khái niệm, chiến lược và phương pháp hay nhất cơ bản để giúp bạn bắt đầu thiết kế câu lệnh nhằm khai thác tối đa các mô hình AI của Gemini.

## Hướng dẫn về câu lệnh theo chủ đề cụ thể

Bạn đang tìm kiếm các chiến lược viết câu lệnh cụ thể hơn? Hãy xem các hướng dẫn khác của chúng tôi về cách viết câu lệnh:

- [Đưa ra câu lệnh bằng tệp đa phương tiện](https://ai.google.dev/gemini-api/docs/files?hl=vi#prompt-guide)
- [Đặt câu lệnh để tạo hình ảnh](https://ai.google.dev/gemini-api/docs/image-generation?hl=vi#prompt-guide)
- [Viết câu lệnh để tạo video](https://ai.google.dev/gemini-api/docs/video?hl=vi#prompt-guide)

Bạn có thể tìm thấy các câu lệnh mẫu khác trong [thư viện câu lệnh](https://ai.google.dev/gemini-api/prompts?hl=vi), được thiết kế để giới thiệu một cách tương tác nhiều khái niệm được chia sẻ trong hướng dẫn này.

## Hướng dẫn rõ ràng và cụ thể

Một cách hiệu quả để tuỳ chỉnh hành vi của mô hình là cung cấp cho mô hình
các hướng dẫn rõ ràng và cụ thể. Chỉ dẫn có thể ở dạng câu hỏi, nhiệm vụ từng bước hoặc phức tạp như việc vạch ra trải nghiệm và tư duy của người dùng.

### Đầu vào

Thông tin đầu vào là văn bản bắt buộc trong câu lệnh mà bạn muốn mô hình đưa ra câu trả lời. Đầu vào có thể là một câu hỏi mà mô hình trả lời (đầu vào câu hỏi), một nhiệm vụ mà mô hình thực hiện (đầu vào nhiệm vụ), một thực thể mà mô hình hoạt động (đầu vào thực thể) hoặc đầu vào một phần mà mô hình hoàn thành hoặc tiếp tục (đầu vào hoàn thành).

| **Loại đầu vào** | **Câu lệnh** | **Nội dung tạo sinh** |
| --- | --- | --- |
| Câu hỏi | ```     What's a good name for a flower shop that specializes in selling bouquets of     dried flowers? Create a list of 5 options with just the names. ``` | ```     Here are 5 names for a flower shop specializing in dried flowers:      1. Everlasting Blooms     2. Dried & Delightful     3. The Petal Preserve     4. Whispers of Wildflowers     5. Forever Blooms ``` |
| Nhiệm vụ | ```     Give me a simple list of just the things that I must bring on a camping trip. The list should have 5 items. ``` | ```     1. **Tent:** Your shelter from the elements.     2. **Sleeping Bag:** Stay warm and comfortable.     3. **Sleeping Pad:** Insulation and cushioning for a good night's sleep.     4. **Headlamp or Flashlight:** Light for nighttime activities.     5. **First Aid Kit:** Be prepared for minor injuries. ``` |
| Thực thể | ```     Classify the following items as [large, small]: Elephant Mouse Snail ``` | ``` Here's the classification:  * **Elephant:** Large * **Mouse:** Small * **Snail:** Small ``` |

#### Tự động hoàn thành một phần nội dung nhập

Mô hình ngôn ngữ tạo sinh hoạt động như một công cụ tự động hoàn thành nâng cao. Khi bạn cung cấp một phần nội dung, mô hình có thể cung cấp phần còn lại của nội dung hoặc nội dung mà mô hình cho là phần tiếp theo của nội dung đó dưới dạng câu trả lời. Khi làm như vậy, nếu bạn đưa ra bất kỳ ví dụ hoặc bối cảnh nào, thì mô hình có thể xem xét các ví dụ hoặc bối cảnh đó.

Ví dụ sau đây cung cấp một câu lệnh có hướng dẫn và dữ liệu đầu vào là thực thể:

|  |
| --- |
| **Câu lệnh:**    ``` For the given order, return a JSON object that has the fields cheeseburger, hamburger, fries, or drink, with the value being the quantity.  Order: A burger and a drink. ```  **Câu trả lời:**    ``` {   "cheeseburger": 0,   "hamburger": 1,   "fries": 0,   "drink": 1 } ```  (gemini-2.5-flash) |

Mặc dù mô hình đã thực hiện theo yêu cầu, nhưng việc viết ra các chỉ dẫn bằng ngôn ngữ tự nhiên đôi khi có thể gặp khó khăn và mô hình sẽ phải tự diễn giải rất nhiều.
Ví dụ: thực đơn của nhà hàng có thể có nhiều món. Để giảm kích thước của phản hồi JSON, có lẽ bạn nên bỏ qua những mặt hàng chưa được đặt hàng. Trong trường hợp này, bạn có thể đưa ra một ví dụ và một tiền tố phản hồi rồi để mô hình hoàn tất:

|  |
| --- |
| **Câu lệnh:**    ``` Valid fields are cheeseburger, hamburger, fries, and drink. Order: Give me a cheeseburger and fries Output: ``` {   "cheeseburger": 1,   "fries": 1 } ``` Order: I want two burgers, a drink, and fries. Output: ```  **Câu trả lời:**    ``` ``` {   "hamburger": 2,   "drink": 1,   "fries": 1 } ``` ```  (gemini-2.5-flash) |

Lưu ý cách "bánh mì kẹp thịt và phô mai" bị loại trừ khỏi đầu ra vì không phải là một phần của đơn đặt hàng.

Mặc dù bạn có thể chỉ định định dạng của các đối tượng phản hồi JSON đơn giản bằng câu lệnh, nhưng bạn nên sử dụng tính năng [đầu ra có cấu trúc](https://ai.google.dev/gemini-api/docs/structured-output?hl=vi) của Gemini API khi chỉ định một giản đồ JSON phức tạp hơn cho phản hồi.

### Giới hạn

Nêu rõ mọi hạn chế đối với việc đọc câu lệnh hoặc tạo câu trả lời. Bạn có thể
cho mô hình biết những việc nên làm và không nên làm. Ví dụ: bạn có thể chỉ định một quy tắc ràng buộc
trong câu lệnh về độ dài của bản tóm tắt:

|  |
| --- |
| **Câu lệnh:**     ``` Summarize this text in one sentence: Text: A quantum computer exploits quantum mechanical phenomena to perform calculations exponentially faster than any modern traditional computer. At very tiny scales, physical matter acts as both particles and as waves, and quantum computing uses specialized hardware to leverage this behavior. The operating principles of quantum devices is beyond the scope of classical physics. When deployed at scale, quantum computers could be used in a wide variety of applications such as: in cybersecurity to break existing encryption methods while helping researchers create new ones, in meteorology to develop better weather forecasting etc. However, the current state of the art quantum computers are still largely experimental and impractical. ```     **Câu trả lời:**     ```       Exploiting quantum mechanical phenomena, quantum computers can perform calculations exponentially faster than traditional computers for potential applications like cybersecurity and meteorology, although they are currently largely experimental and impractical. ```  (gemini-2.5-flash) |

### Định dạng của phản hồi

Bạn có thể đưa ra chỉ dẫn nêu rõ định dạng của câu trả lời. Ví dụ:
bạn có thể yêu cầu định dạng câu trả lời dưới dạng bảng, danh sách có dấu đầu dòng, quảng cáo chiêu hàng cô đọng,
từ khoá, câu hoặc đoạn văn. Chỉ dẫn hệ thống sau đây yêu cầu mô hình phản hồi theo cách trò chuyện hơn:

|  |
| --- |
| **Chỉ dẫn hệ thống**    ```     All questions should be answered comprehensively with details, unless the user requests a concise response specifically. ```  **Câu lệnh**    ```     What is a smart way to make a business that sells DVD's in 2026? ```  **Câu trả lời:**    ``` Starting a business selling DVDs in 2026 presents significant challenges due to the overwhelming dominance of digital streaming and on-demand services; a "smart" approach would therefore require a highly specialized niche, a strong value proposition beyond just the disc, and likely a focus on community or collector markets rather than mainstream consumption.  Here's a breakdown of what a smart DVD business in 2026 would likely entail:  1. Extreme Niche Specialization: You cannot compete with streaming libraries. Your business must focus on what digital doesn't offer easily or at all. This could include:      * Out-of-Print & Rare Titles: Sourcing films or TV shows that have never been released digitally or are currently unavailable on major streaming platforms.     .... ```  (gemini-2.5-flash) |

#### Định dạng câu trả lời bằng chiến lược hoàn thành

[Chiến lược hoàn thành](#completion) cũng có thể giúp định dạng câu trả lời.
Ví dụ sau đây yêu cầu mô hình tạo dàn ý cho một bài luận:

|  |
| --- |
| **Câu lệnh:**    ``` Create an outline for an essay about hummingbirds. ```  **Câu trả lời:**    ``` Here is a possible outline for an essay about hummingbirds:  I. Introduction A. Hook: Start with a captivating fact or description about hummingbirds (e.g., their speed, iridescent colors, or tiny size). B. Background: Briefly introduce hummingbirds – where they are found (Americas), their reputation as unique birds. C. Thesis Statement: State the main point of the essay, which could be about the remarkable adaptations, behaviors, and ecological importance of hummingbirds.  II. Appearance and Identification ..... ```  (gemini-2.5-flash) |

Câu lệnh không chỉ định định dạng cho dàn ý và mô hình đã chọn một định dạng cho bạn. Để yêu cầu mô hình trả về một dàn ý theo một định dạng cụ thể, bạn có thể thêm văn bản đại diện cho phần đầu của dàn ý và để mô hình hoàn thành dàn ý đó dựa trên mẫu mà bạn đã bắt đầu.

|  |
| --- |
| **Câu lệnh:**    ``` Create an outline for an essay about hummingbirds. I. Introduction    * ```  **Câu trả lời:**    ``` Okay, here is an outline for an essay about hummingbirds, starting from the introduction you provided:  I. Introduction * Hook: Start with a captivating fact or description about hummingbirds (e.g., their speed, iridescent colors, or tiny size). * Background: Briefly introduce hummingbirds – where they are found (Americas), their reputation as unique birds, and their general characteristics. * Thesis Statement: State the main point of the essay, focusing on the remarkable adaptations, behaviors, and ecological significance that make hummingbirds extraordinary. ..... ```  (gemini-2.5-flash) |

## Câu lệnh không có ví dụ so với đặt câu lệnh dựa trên một vài ví dụ

Bạn có thể đưa các ví dụ vào câu lệnh để cho mô hình biết kết quả đúng trông như thế nào. Mô hình này cố gắng xác định các mẫu và mối quan hệ từ các ví dụ, sau đó áp dụng chúng khi tạo câu trả lời. Câu lệnh chứa một vài ví dụ được gọi là câu lệnh *few-shot*, còn câu lệnh không đưa ra ví dụ nào được gọi là câu lệnh *zero-shot*. Câu lệnh dựa trên một vài ví dụ thường được dùng để điều chỉnh định dạng, cách diễn đạt, phạm vi hoặc mẫu chung của câu trả lời của mô hình. Sử dụng các ví dụ cụ thể và đa dạng để giúp mô hình thu hẹp phạm vi tập trung và tạo ra kết quả chính xác hơn.

Bạn nên luôn đặt câu lệnh kèm một vài ví dụ về few-shot vào câu lệnh. Câu lệnh không có đặt câu lệnh kèm một vài ví dụ có thể sẽ kém hiệu quả hơn. Trên thực tế, bạn có thể xoá hướng dẫn khỏi câu lệnh nếu các ví dụ của bạn đủ rõ ràng để cho thấy nhiệm vụ cần thực hiện.

Câu lệnh zero-shot sau đây yêu cầu mô hình chọn nội dung giải thích phù hợp nhất.

|  |
| --- |
| **Câu lệnh:**    ``` Please choose the best explanation to the question:  Question: How is snow formed? Explanation1: Snow is formed when water vapor in the air freezes into ice crystals in the atmosphere, which can combine and grow into snowflakes as they fall through the atmosphere and accumulate on the ground. Explanation2: Water vapor freezes into ice crystals forming snow. Answer: ```  **Câu trả lời:**    ``` Explanation1 is the better explanation because it provides more detail on the process, including how ice crystals combine and grow into snowflakes as they fall through the atmosphere. ```  (gemini-2.5-flash) |

Nếu trường hợp sử dụng của bạn yêu cầu mô hình tạo ra câu trả lời ngắn gọn, bạn có thể đưa các ví dụ vào câu lệnh ưu tiên câu trả lời ngắn gọn.

Câu lệnh sau đây đưa ra hai ví dụ cho thấy sự ưu tiên đối với các nội dung giải thích ngắn hơn. Trong câu trả lời, bạn có thể thấy rằng các ví dụ đã hướng dẫn mô hình chọn nội dung giải thích ngắn hơn (`Explanation2`) thay vì nội dung giải thích dài hơn (`Explanation1`) như trước đây.

|  |
| --- |
| **Câu lệnh:**    ``` Below are some examples showing a question, explanation, and answer format:  Question: Why is the sky blue? Explanation1: The sky appears blue because of Rayleigh scattering, which causes shorter blue wavelengths of light to be scattered more easily than longer red wavelengths, making the sky look blue. Explanation2: Due to Rayleigh scattering effect. Answer: Explanation2  Question: What is the cause of earthquakes? Explanation1: Sudden release of energy in the Earth's crust. Explanation2: Earthquakes happen when tectonic plates suddenly slip or break apart, causing a release of energy that creates seismic waves that can shake the ground and cause damage. Answer: Explanation1  Now, Answer the following question given the example formats above:  Question: How is snow formed? Explanation1: Snow is formed when water vapor in the air freezes into ice crystals in the atmosphere, which can combine and grow into snowflakes as they fall through the atmosphere and accumulate on the ground. Explanation2: Water vapor freezes into ice crystals forming snow. Answer: ```  **Câu trả lời:**    ``` Answer: Explanation2 ```  (gemini-2.5-flash) |

### Số lượng ví dụ tối ưu

Các mô hình như Gemini thường có thể nhận ra các mẫu bằng cách sử dụng một vài ví dụ, mặc dù bạn có thể cần thử nghiệm với số lượng ví dụ cần cung cấp trong câu lệnh để có kết quả tốt nhất. Đồng thời, nếu bạn đưa ra quá nhiều ví dụ, mô hình có thể bắt đầu [điều chỉnh quá mức](https://developers.google.com/machine-learning/glossary?hl=vi#overfitting) phản hồi cho các ví dụ.

### Định dạng nhất quán

Đảm bảo rằng cấu trúc và định dạng của các ví dụ trong câu lệnh kèm một vài ví dụ là giống nhau để tránh nhận được câu trả lời có định dạng không mong muốn. Một trong những mục tiêu chính của việc thêm
ví dụ ít lần trong câu lệnh là cho mô hình thấy định dạng phản hồi. Do đó, bạn cần đảm bảo định dạng nhất quán trên tất cả các ví dụ, đặc biệt là chú ý đến thẻ XML, khoảng trắng, dòng mới và dấu phân cách ví dụ.

## Thêm bối cảnh

Bạn có thể đưa hướng dẫn và thông tin vào câu lệnh mà mô hình cần để giải quyết vấn đề, thay vì giả định rằng mô hình có tất cả thông tin cần thiết. Thông tin theo bối cảnh này giúp mô hình hiểu được các ràng buộc và thông tin chi tiết về những việc bạn yêu cầu mô hình thực hiện.

Ví dụ sau đây yêu cầu mô hình đưa ra hướng dẫn khắc phục sự cố cho bộ định tuyến:

|  |
| --- |
| **Câu lệnh:**    ``` What should I do to fix my disconnected wifi? The light on my Google Wifi router is yellow and blinking slowly. ```  **Câu trả lời:**    ```   A yellow blinking light on your Google Wifi router usually indicates a problem   with the internet connection. Here are some steps to troubleshoot and fix the   issue:   1. Restart your router and modem:     - Unplug your modem from the power outlet and wait for 30 seconds.     - Plug your modem back in and wait for it to fully boot up.     - Unplug your Google Wifi router and wait for 30 seconds.     - Plug your Google Wifi router back in and wait for it to fully boot up. ..... ```  (gemini-2.5-flash) |

Câu trả lời có vẻ là thông tin khắc phục sự cố chung chung, không cụ thể cho bộ định tuyến hoặc trạng thái của đèn chỉ báo LED.

Để tuỳ chỉnh câu trả lời cho bộ định tuyến cụ thể, bạn có thể thêm hướng dẫn khắc phục sự cố của bộ định tuyến vào câu lệnh để Gemini tham khảo khi đưa ra câu trả lời.

|  |
| --- |
| **Câu lệnh:**    ``` Answer the question using the text below. Respond with only the text provided. Question: What should I do to fix my disconnected wifi? The light on my Google Wifi router is yellow and blinking slowly.  Text: Color: Slowly pulsing yellow What it means: There is a network error. What to do: Check that the Ethernet cable is connected to both your router and your modem and both devices are turned on. You might need to unplug and plug in each device again.  Color: Fast blinking yellow What it means: You are holding down the reset button and are factory resetting this device. What to do: If you keep holding down the reset button, after about 12 seconds, the light will turn solid yellow. Once it is solid yellow, let go of the factory reset button.  Color: Solid yellow What it means: Router is factory resetting. What to do: This can take up to 10 minutes. When it's done, the device will reset itself and start pulsing white, letting you know it's ready for setup.  Color: Solid red What it means: Something is wrong. What to do: Critical failure. Factory reset the router. If the light stays red, contact Wifi customer support. ```  **Câu trả lời:**    ``` Check that the Ethernet cable is connected to both your router and your modem and both devices are turned on. You might need to unplug and plug in each device again. ```  (gemini-2.5-flash) |

## Chia câu lệnh thành các thành phần

Đối với những trường hợp sử dụng yêu cầu câu lệnh phức tạp, bạn có thể giúp mô hình quản lý độ phức tạp này bằng cách chia nhỏ thành các thành phần đơn giản hơn.

1. **Chia nhỏ chỉ dẫn:** Thay vì đưa ra nhiều chỉ dẫn trong một câu lệnh, hãy tạo một câu lệnh cho mỗi chỉ dẫn. Bạn có thể chọn câu lệnh để xử lý dựa trên thông tin đầu vào của người dùng.
2. **Chuỗi câu lệnh:** Đối với những tác vụ phức tạp liên quan đến nhiều bước tuần tự, hãy tạo một câu lệnh cho mỗi bước và liên kết các câu lệnh với nhau theo một trình tự. Trong chuỗi câu lệnh tuần tự này, đầu ra của một câu lệnh trong chuỗi sẽ trở thành đầu vào của câu lệnh tiếp theo. Đầu ra của câu lệnh cuối cùng trong chuỗi là đầu ra cuối cùng.
3. **Phản hồi tổng hợp:** Tổng hợp là khi bạn muốn thực hiện nhiều tác vụ song song trên nhiều phần dữ liệu và tổng hợp kết quả để tạo ra kết quả cuối cùng. Ví dụ: bạn có thể yêu cầu mô hình thực hiện một thao tác trên phần đầu tiên của dữ liệu, thực hiện một thao tác khác trên phần còn lại của dữ liệu và tổng hợp kết quả.

## Thử nghiệm với các tham số mô hình

Mỗi lệnh gọi mà bạn gửi đến một mô hình đều bao gồm các giá trị tham số kiểm soát cách
mô hình tạo phản hồi. Mô hình có thể tạo ra các kết quả khác nhau cho
các giá trị tham số khác nhau. Hãy thử nghiệm với nhiều giá trị tham số để có được giá trị phù hợp nhất cho nhiệm vụ. Các tham số có sẵn cho các mô hình khác nhau có thể khác nhau. Sau đây là các tham số phổ biến nhất:

1. **Số mã thông báo đầu ra tối đa:** Chỉ định số lượng mã thông báo tối đa có thể được tạo trong phản hồi. Một mã thông báo có khoảng 4 ký tự. 100 token tương đương với khoảng 60-80 từ.
2. **Nhiệt độ:** Nhiệt độ kiểm soát mức độ ngẫu nhiên trong việc chọn mã thông báo. Nhiệt độ được dùng để lấy mẫu trong quá trình tạo phản hồi,
   xảy ra khi áp dụng `topP` và `topK`. Nhiệt độ thấp phù hợp với những câu lệnh yêu cầu câu trả lời mang tính tất định hơn hoặc ít mở hơn, trong khi nhiệt độ cao có thể dẫn đến kết quả đa dạng hoặc sáng tạo hơn. Nhiệt độ 0 là xác định, tức là phản hồi có xác suất cao nhất luôn được chọn.
3. **`topK`:** Tham số `topK` thay đổi cách mô hình chọn mã thông báo cho đầu ra. `topK` bằng 1 có nghĩa là mã thông báo đã chọn có khả năng xuất hiện cao nhất trong số tất cả mã thông báo trong từ vựng của mô hình (còn gọi là giải mã tham lam), trong khi `topK` bằng 3 có nghĩa là mã thông báo tiếp theo được chọn trong số 3 mã thông báo có khả năng xuất hiện cao nhất bằng cách sử dụng nhiệt độ. Đối với mỗi bước chọn mã thông báo, các mã thông báo `topK` có xác suất cao nhất sẽ được lấy mẫu. Sau đó, các mã thông báo sẽ được lọc thêm dựa trên `topP`, mã thông báo cuối cùng được chọn bằng cách sử dụng phương pháp lấy mẫu nhiệt độ.
4. **`topP`:** Tham số `topP` thay đổi cách mô hình chọn mã thông báo cho đầu ra. Các mã thông báo được chọn từ có khả năng cao nhất đến ít có khả năng nhất cho đến khi tổng xác suất của chúng bằng giá trị `topP`. Ví dụ: nếu mã thông báo A, B và C có xác suất lần lượt là 0,3, 0,2 và 0,1, còn giá trị `topP` là 0,5, thì mô hình sẽ chọn A hoặc B làm mã thông báo tiếp theo bằng cách sử dụng nhiệt độ và loại trừ C khỏi danh sách đề xuất. Giá trị `topP` mặc định là 0,95.
5. **`stop_sequences`:** Đặt trình tự dừng để yêu cầu mô hình ngừng tạo nội dung. Chuỗi dừng có thể là bất kỳ chuỗi ký tự nào. Cố gắng tránh sử dụng một chuỗi ký tự có thể xuất hiện trong nội dung được tạo.

## Chiến lược ra lệnh nối tiếp

Đôi khi, bạn cần phải lặp lại thiết kế câu lệnh vài lần trước khi nhận được câu trả lời như mong muốn một cách nhất quán. Phần này hướng dẫn một số việc bạn có thể thử khi lặp lại câu lệnh:

1. **Sử dụng cách diễn đạt khác:** Việc sử dụng các từ hoặc cách diễn đạt khác nhau trong câu lệnh thường mang lại các câu trả lời khác nhau từ mô hình, mặc dù tất cả đều có nghĩa giống nhau. Nếu bạn không nhận được kết quả như mong đợi từ câu lệnh, hãy thử diễn đạt lại câu lệnh đó.

   |  |
   | --- |
   | ``` Version 1: How do I bake a pie?  Version 2: Suggest a recipe for a pie.  Version 3: What's a good pie recipe? ``` |
2. **Chuyển sang một nhiệm vụ tương tự:** Nếu bạn không thể yêu cầu mô hình làm theo hướng dẫn của mình cho một nhiệm vụ, hãy thử đưa ra hướng dẫn cho một nhiệm vụ tương tự để đạt được cùng một kết quả.

   Câu lệnh này yêu cầu mô hình phân loại một cuốn sách bằng cách sử dụng các danh mục được xác định trước:

   |  |
   | --- |
   | **Câu lệnh:**    ``` Which category does The Odyssey belong to: thriller sci-fi mythology biography ```  **Câu trả lời:**    ```     The Odyssey belongs to the category of **mythology**.       Here's why:      * **Mythology:** The Odyssey tells the story of Odysseus, a hero from Greek mythology, and his     journey home after the Trojan War. It features gods, monsters, and supernatural events common to     Greek mythology. ..... ```  (gemini-2.5-flash) |

   Câu trả lời đúng, nhưng mô hình không nằm trong phạm vi của các lựa chọn. Bạn cũng muốn mô hình chỉ phản hồi bằng một trong các lựa chọn thay vì một câu đầy đủ. Trong trường hợp này, bạn có thể diễn đạt lại hướng dẫn dưới dạng câu hỏi trắc nghiệm và yêu cầu mô hình chọn một phương án.

   |  |
   | --- |
   | **Câu lệnh:**    ``` Multiple choice problem: Which of the following options describes the book The Odyssey? Options: ``` |

   - thriller
   - sci-fi
   - mythology
   - biography
     **Câu trả lời:**

     ```
     The correct answer is mythology.
     ```

     (gemini-2.5-flash)
   - **Thay đổi thứ tự nội dung câu lệnh:** Thứ tự nội dung trong câu lệnh đôi khi có thể ảnh hưởng đến câu trả lời. Hãy thử thay đổi thứ tự nội dung và xem điều đó ảnh hưởng như thế nào đến câu trả lời.

     ```
     Version 1:
     [examples]
     [context]
     [input]

     Version 2:
     [input]
     [examples]
     [context]

     Version 3:
     [examples]
     [input]
     [context]
     ```

## Câu trả lời dự phòng

Câu trả lời dự phòng là câu trả lời do mô hình trả về khi câu lệnh hoặc câu trả lời kích hoạt bộ lọc an toàn. Ví dụ về câu trả lời dự phòng là "Tôi không thể giúp bạn việc đó vì tôi chỉ là một mô hình ngôn ngữ".

Nếu mô hình phản hồi bằng một câu trả lời dự phòng, hãy thử tăng nhiệt độ.

## Căn cứ và thực thi mã

Gemini có thể sử dụng các công cụ để tránh đưa ra thông tin sai lệch trong những trường hợp mà Gemini có thể đưa ra câu trả lời không chính xác.

Tính năng [Neo bám vào Google Tìm kiếm](https://ai.google.dev/gemini-api/docs/google-search?hl=vi) kết nối mô hình Gemini với nội dung trên web theo thời gian thực và nên được bật bất cứ khi nào mô hình có thể cần biết các thông tin thực tế gần đây hoặc không rõ ràng.

[Công cụ thực thi mã](https://ai.google.dev/gemini-api/docs/code-execution?hl=vi) của Gemini cho phép mô hình tạo và chạy mã Python, đồng thời cần được bật bất cứ khi nào mô hình cần thực hiện bất kỳ phép tính, phép đếm hoặc phép tính nào.

## Gemini 3

[Các mô hình Gemini 3](https://ai.google.dev/gemini-api/docs/models?hl=vi#gemini-3) được thiết kế để suy luận nâng cao và làm theo chỉ dẫn.
Mô hình này phản hồi tốt nhất với những câu lệnh trực tiếp, có cấu trúc tốt và xác định rõ nhiệm vụ cũng như mọi quy tắc ràng buộc. Bạn nên áp dụng các phương pháp sau đây để đạt được kết quả tối ưu khi dùng Gemini 3:

### Nguyên tắc cốt lõi về câu lệnh

- **Chính xác và trực tiếp:** Nêu rõ mục tiêu của bạn một cách rõ ràng và súc tích. Tránh dùng ngôn từ không cần thiết hoặc mang tính thuyết phục quá mức.
- **Sử dụng cấu trúc nhất quán:** Sử dụng dấu phân cách rõ ràng để phân tách các phần khác nhau trong câu lệnh của bạn. Các thẻ kiểu XML (ví dụ: `<context>`, `<task>`) hoặc tiêu đề Markdown đều có hiệu quả. Chọn một định dạng và sử dụng định dạng đó một cách nhất quán trong một câu lệnh.
- **Xác định các tham số:** Giải thích rõ ràng mọi thuật ngữ hoặc tham số không rõ ràng.
- **Kiểm soát độ chi tiết của đầu ra:** Theo mặc định, các mô hình Gemini 3 sẽ đưa ra câu trả lời trực tiếp và
  hiệu quả. Nếu cần câu trả lời chi tiết hoặc mang tính trò chuyện hơn,
  bạn phải yêu cầu rõ ràng trong phần chỉ dẫn.
- **Xử lý dữ liệu đầu vào đa phương thức một cách nhất quán:** Khi sử dụng văn bản, hình ảnh, âm thanh hoặc video, hãy coi chúng là dữ liệu đầu vào có cùng cấp độ. Đảm bảo hướng dẫn của bạn tham chiếu rõ ràng đến từng phương thức khi cần.
- **Ưu tiên các chỉ dẫn quan trọng:** Đặt các quy tắc ràng buộc thiết yếu về hành vi, định nghĩa vai trò (vai trò) và yêu cầu về định dạng đầu ra trong Chỉ dẫn hệ thống hoặc ở ngay đầu câu lệnh của người dùng.
- **Cấu trúc cho bối cảnh dài:** Khi cung cấp lượng lớn bối cảnh (ví dụ: tài liệu, mã), hãy cung cấp tất cả bối cảnh trước. Đặt chỉ dẫn hoặc câu hỏi cụ thể của bạn ở ngay *cuối* câu lệnh.
- **Cố định bối cảnh:** Sau một khối dữ liệu lớn, hãy sử dụng một cụm từ chuyển tiếp rõ ràng để kết nối bối cảnh với câu hỏi của bạn, chẳng hạn như "Dựa trên thông tin ở trên..."

### Chiến lược Gemini 3 Flash

- **Độ chính xác của ngày hiện tại:** Thêm mệnh đề sau vào hướng dẫn cho hệ thống để giúp mô hình chú ý đến ngày hiện tại là năm 2026:

  ```
  For time-sensitive user queries that require up-to-date information, you
  MUST follow the provided current time (date and year) when formulating
  search queries in tool calls. Remember it is 2026 this year.
  ```
- **Độ chính xác của ngày ngừng cập nhật kiến thức:** Thêm mệnh đề sau vào chỉ dẫn hệ thống để mô hình biết về ngày ngừng cập nhật kiến thức của mình:

  ```
  Your knowledge cutoff date is January 2025.
  ```
- **Hiệu suất cơ sở:** Thêm mệnh đề sau vào hướng dẫn hệ thống (chỉnh sửa nếu thích hợp) để cải thiện khả năng cơ sở của mô hình trong ngữ cảnh được cung cấp:

  ```
  You are a strictly grounded assistant limited to the information provided in
  the User Context. In your answers, rely **only** on the facts that are
  directly mentioned in that context. You must **not** access or utilize your
  own knowledge or common sense to answer. Do not assume or infer from the
  provided facts; simply report them exactly as they appear. Your answer must
  be factual and fully truthful to the provided text, leaving absolutely no
  room for speculation or interpretation. Treat the provided context as the
  absolute limit of truth; any facts or details that are not directly
  mentioned in the context must be considered **completely untruthful** and
  **completely unsupported**. If the exact answer is not explicitly written in
  the context, you must state that the information is not available.
  ```

### Nâng cao khả năng suy luận và lập kế hoạch

Các mô hình thuộc dòng Gemini 2.5 và 3 tự động tạo văn bản "suy nghĩ" nội bộ để cải thiện hiệu suất suy luận. Do đó, thường không cần thiết phải có
mô hình phác thảo, lập kế hoạch hoặc trình bày chi tiết các bước suy luận trong phản hồi được trả về. Đối với những vấn đề đòi hỏi khả năng suy luận cao, những yêu cầu đơn giản như "Hãy suy nghĩ thật kỹ trước khi trả lời" có thể cải thiện hiệu suất, mặc dù phải tốn thêm token tư duy.

Hãy xem tài liệu về [quy trình tư duy của Gemini](https://ai.google.dev/gemini-api/docs/thinking?hl=vi) để biết thêm thông tin chi tiết.

### Ví dụ về câu lệnh có cấu trúc

Việc sử dụng thẻ hoặc Markdown giúp mô hình phân biệt giữa hướng dẫn, bối cảnh và nhiệm vụ.

**Ví dụ về XML:**

```
<role>
You are a helpful assistant.
</role>

<constraints>
1. Be objective.
2. Cite sources.
</constraints>

<context>
[Insert User Input Here - The model knows this is data, not instructions]
</context>

<task>
[Insert the specific user request here]
</task>
```

**Ví dụ về Markdown:**

```
# Identity
You are a senior solution architect.

# Constraints
- No external libraries allowed.
- Python 3.11+ syntax only.

# Output format
Return a single code block.
```

### Mẫu ví dụ kết hợp các phương pháp hay nhất

Mẫu này ghi lại các nguyên tắc cốt lõi để đưa ra câu lệnh cho Gemini 3. Luôn đảm bảo lặp lại và sửa đổi cho trường hợp sử dụng cụ thể của bạn.

**Chỉ dẫn hệ thống:**

```
<role>
You are Gemini 3, a specialized assistant for [Insert Domain, e.g., Data Science].
You are precise, analytical, and persistent.
</role>

<instructions>
1. **Plan**: Analyze the task and create a step-by-step plan.
2. **Execute**: Carry out the plan.
3. **Validate**: Review your output against the user's task.
4. **Format**: Present the final answer in the requested structure.
</instructions>

<constraints>
- Verbosity: [Specify Low/Medium/High]
- Tone: [Specify Formal/Casual/Technical]
</constraints>

<output_format>
Structure your response as follows:
1. **Executive Summary**: [Short overview]
2. **Detailed Response**: [The main content]
</output_format>
```

**Câu lệnh của người dùng:**

```
<context>
[Insert relevant documents, code snippets, or background info here]
</context>

<task>
[Insert specific user request here]
</task>

<final_instruction>
Remember to think step-by-step before answering.
</final_instruction>
```

## Quy trình công việc dựa trên tác nhân

Đối với quy trình làm việc sâu của tác nhân, bạn thường cần có hướng dẫn cụ thể để kiểm soát cách mô hình suy luận, lập kế hoạch và thực hiện các tác vụ. Mặc dù Gemini mang lại hiệu suất chung mạnh mẽ, nhưng các tác nhân phức tạp thường yêu cầu bạn định cấu hình sự đánh đổi giữa chi phí tính toán (độ trễ và mã thông báo) và độ chính xác của tác vụ.

Khi thiết kế câu lệnh cho tác nhân, hãy cân nhắc các khía cạnh hành vi sau đây mà bạn có thể điều khiển trong tác nhân:

### Lập luận và chiến lược

Cấu hình cho cách mô hình suy nghĩ và lập kế hoạch trước khi hành động.

- **Phân tích logic:** Xác định mức độ kỹ lưỡng mà mô hình phải phân tích các quy tắc ràng buộc, điều kiện tiên quyết và thứ tự thực hiện phép tính.
- **Chẩn đoán vấn đề**: Kiểm soát mức độ phân tích sâu khi xác định nguyên nhân và việc mô hình sử dụng suy luận suy đoán. Xác định xem mô hình có nên chấp nhận câu trả lời rõ ràng nhất hay khám phá những lời giải thích phức tạp, ít có khả năng xảy ra hơn.
- **Tính đầy đủ của thông tin:** Sự đánh đổi giữa việc phân tích mọi chính sách và tài liệu hiện có với việc ưu tiên hiệu quả và tốc độ.

### Thực thi và độ tin cậy

Cấu hình cho cách tác nhân hoạt động độc lập và xử lý các trở ngại.

- **Khả năng thích ứng:** Cách mô hình phản ứng với dữ liệu mới. Xác định xem có nên tuân thủ nghiêm ngặt kế hoạch ban đầu hay chuyển hướng ngay lập tức khi kết quả quan sát mâu thuẫn với giả định.
- **Tính bền bỉ và khả năng khôi phục:** Mức độ mà mô hình cố gắng tự sửa lỗi. Mức độ bền bỉ cao giúp tăng tỷ lệ thành công nhưng có nguy cơ làm tăng chi phí mã thông báo hoặc gây ra vòng lặp.
- **Đánh giá rủi ro:** Logic để đánh giá hậu quả. Phân biệt rõ ràng giữa các thao tác khám phá có rủi ro thấp (đọc) và các thay đổi trạng thái có rủi ro cao (ghi).

### Tương tác và đầu ra

Cấu hình về cách tác nhân giao tiếp với người dùng và định dạng kết quả.

- **Xử lý sự mơ hồ và quyền:** Xác định thời điểm mô hình được phép đưa ra giả định so với thời điểm mô hình phải tạm dừng thực thi để yêu cầu người dùng làm rõ hoặc cấp quyền.
- **Độ chi tiết:** Kiểm soát lượng văn bản được tạo cùng với các lệnh gọi công cụ. Điều này xác định xem mô hình có giải thích hành động của mình cho người dùng hay không hoặc vẫn im lặng trong quá trình thực thi.
- **Độ chính xác và đầy đủ:** Độ chính xác cần thiết của kết quả đầu ra. Xác định xem mô hình có phải giải quyết mọi trường hợp đặc biệt và cung cấp số liệu chính xác hay không, hoặc có thể chấp nhận số liệu ước tính sơ bộ.

### Mẫu hướng dẫn hệ thống

Chỉ dẫn hệ thống sau đây là một ví dụ đã được các nhà nghiên cứu đánh giá để cải thiện hiệu suất trên các điểm chuẩn của tác nhân, trong đó mô hình phải tuân thủ một bộ quy tắc phức tạp và tương tác với người dùng. Điều này khuyến khích tác nhân đóng vai trò là một người lập luận và lập kế hoạch hiệu quả, thực thi các hành vi cụ thể trên các phương diện nêu trên và yêu cầu mô hình chủ động lập kế hoạch trước khi thực hiện bất kỳ hành động nào.

Bạn có thể điều chỉnh mẫu này cho phù hợp với các quy tắc ràng buộc cụ thể trong trường hợp sử dụng của mình.

```
You are a very strong reasoner and planner. Use these critical instructions to structure your plans, thoughts, and responses.

Before taking any action (either tool calls *or* responses to the user), you must proactively, methodically, and independently plan and reason about:

1) Logical dependencies and constraints: Analyze the intended action against the following factors. Resolve conflicts in order of importance:
    1.1) Policy-based rules, mandatory prerequisites, and constraints.
    1.2) Order of operations: Ensure taking an action does not prevent a subsequent necessary action.
        1.2.1) The user may request actions in a random order, but you may need to reorder operations to maximize successful completion of the task.
    1.3) Other prerequisites (information and/or actions needed).
    1.4) Explicit user constraints or preferences.

2) Risk assessment: What are the consequences of taking the action? Will the new state cause any future issues?
    2.1) For exploratory tasks (like searches), missing *optional* parameters is a LOW risk. **Prefer calling the tool with the available information over asking the user, unless** your `Rule 1` (Logical Dependencies) reasoning determines that optional information is required for a later step in your plan.

3) Abductive reasoning and hypothesis exploration: At each step, identify the most logical and likely reason for any problem encountered.
    3.1) Look beyond immediate or obvious causes. The most likely reason may not be the simplest and may require deeper inference.
    3.2) Hypotheses may require additional research. Each hypothesis may take multiple steps to test.
    3.3) Prioritize hypotheses based on likelihood, but do not discard less likely ones prematurely. A low-probability event may still be the root cause.

4) Outcome evaluation and adaptability: Does the previous observation require any changes to your plan?
    4.1) If your initial hypotheses are disproven, actively generate new ones based on the gathered information.

5) Information availability: Incorporate all applicable and alternative sources of information, including:
    5.1) Using available tools and their capabilities
    5.2) All policies, rules, checklists, and constraints
    5.3) Previous observations and conversation history
    5.4) Information only available by asking the user

6) Precision and Grounding: Ensure your reasoning is extremely precise and relevant to each exact ongoing situation.
    6.1) Verify your claims by quoting the exact applicable information (including policies) when referring to them. 

7) Completeness: Ensure that all requirements, constraints, options, and preferences are exhaustively incorporated into your plan.
    7.1) Resolve conflicts using the order of importance in #1.
    7.2) Avoid premature conclusions: There may be multiple relevant options for a given situation.
        7.2.1) To check for whether an option is relevant, reason about all information sources from #5.
        7.2.2) You may need to consult the user to even know whether something is applicable. Do not assume it is not applicable without checking.
    7.3) Review applicable sources of information from #5 to confirm which are relevant to the current state.

8) Persistence and patience: Do not give up unless all the reasoning above is exhausted.
    8.1) Don't be dissuaded by time taken or user frustration.
    8.2) This persistence must be intelligent: On *transient* errors (e.g. please try again), you *must* retry **unless an explicit retry limit (e.g., max x tries) has been reached**. If such a limit is hit, you *must* stop. On *other* errors, you must change your strategy or arguments, not repeat the same failed call.

9) Inhibit your response: only take an action after all the above reasoning is completed. Once you've taken an action, you cannot take it back.
```

## Các bước tiếp theo

- Giờ đây, khi đã hiểu rõ hơn về thiết kế câu lệnh, hãy thử viết câu lệnh của riêng bạn bằng [Google AI Studio](http://aistudio.google.com?hl=vi).
- Để tìm hiểu về câu lệnh đa phương thức, hãy xem bài viết [Đưa ra câu lệnh bằng tệp đa phương tiện](https://ai.google.dev/gemini-api/docs/files?hl=vi#prompt-guide).
- Để tìm hiểu về câu lệnh tạo hình ảnh, hãy xem hướng dẫn về câu lệnh của [Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=vi#prompt-guide).
- Để tìm hiểu về cách viết câu lệnh cho video, hãy xem [hướng dẫn về câu lệnh cho Veo](https://ai.google.dev/gemini-api/docs/video?hl=vi#prompt-guide).

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-10-13 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-10-13 UTC."],[],[]]
