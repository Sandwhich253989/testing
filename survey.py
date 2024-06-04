import re

survey_response = """
### Type of condition you are dealing with?

Headaches


### On a scale of 1-10, how would you rate the severity of your headaches?

1-3: Mild pain


### How long have you been experiencing headaches?

6-12 months


### How frequently do you experience headaches?

Daily constant


### Does your headaches get worse with certain activities?

Working; sitting or standing in one place for an extended period of time


### How would you describe the type of pain you're experiencing?

Sharp


### Have you tried any treatments or remedies for your headaches? If so, which ones?

Chiropractic adjustments


### Have you ever been diagnosed with a neurological condition, such as migraines or tension headaches, causing persistent head pain?

Yes


### Does your headache pain radiate? Do you experience any associated symptoms such as visual disturbances, nausea, or sensitivity to light and sound?

Yes


### Have you recently experienced any trauma or injury to your head?

Yes, within the past week


### How has your headaches affected your daily activities and quality of life?

I can't perform any activities due to the pain


### What is your age group?

35-44 years old


### How committed are you to fix this pain today?

Very committed


### First name

aravind


### Last name

sai


### Phone number

+12018965652


### Email

abc@gmail.com


### Counter_05d7afa7_c76a_4748_907e_674d46f9d0f7 (variable)

0


### Counter_1d1bd8a6_45c2_434d_893a_0593d68567f3 (variable)

0


### Counter_e779f2a6_6c6f_4af6_9127_10f9658e2a31 (variable)

0


### Counter_f819c69b_b1ba_4567_8a66_6c8b409d7d98 (variable)

0


### Score (variable)

37


### Winning_outcome_id (variable)

lNyohwh7BNmd


### Outcome ID

lNyohwh7BNmd


### Outcome Title

Significant Dysfunction

If your health quiz flagged you in the "Significant Dysfunction" category, it's time to face it head-on – but worry not, because I'm here to guide you through this challenge.

I'm Dr. Luke Stringer, and my commitment is to help you conquer significant dysfunction and pave the way for a life free from the chains of discomfort.
A significant dysfunction is not a moment to take lightly. It's a call to action, and your first step is urgent – seek professional intervention for a thorough assessment. That's where I come in, ready to bring my expertise to the table and unravel the complexities of your situation.

Consider diagnostic assessments to identify underlying causes. We're not just treating symptoms; we're on a mission to understand the root of the issue, ensuring a comprehensive and effective approach to your well-being.

Now, let's talk about treatment plans. Following a prescribed plan is crucial, and in your case, it may include physical therapy. This isn't just about alleviating discomfort; it's about restoring function and reclaiming your life.

The next crucial move? A personalized consultation with us at Advanced Health Chiropractic. Here, we'll conduct a detailed assessment, discuss your symptoms, and chart a course towards meaningful improvement.

Our team has been the beacon for countless individuals navigating the path to relief, and I'm confident we can be the same guiding force for you.

But here's the deal – our consultation slots are more precious than gold. Once they're filled, they're filled.

Don't let your pain dictate the terms of your life. Check that calendar below, secure your spot for a consultation, and let's ignite the journey to a life unburdened by the weight of discomfort.

Your transformation starts now. Click, book, and let's script a powerful comeback together.
"""

first_name = re.findall(r'\bFirst\sn\b\s\n(\b\w*\b)', survey_response,flags=re.IGNORECASE)
print(f"first name: {first_name}")

last_name = re.findall(r'\bLast\sname\b\s\n(\b\w*\b)', survey_response,flags=re.IGNORECASE)
print(f"last name: {last_name}")

phone_number = re.findall(r'\bPhone\snumber\b\s\n(.*)', survey_response,flags=re.IGNORECASE)
print(f"phone number: {phone_number}")

email = re.findall(r'\bEmail\b\s\n(\b.*\b)', survey_response,flags=re.IGNORECASE)
print(f"email: {email}")
