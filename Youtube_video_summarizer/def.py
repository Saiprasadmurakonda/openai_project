from youtube_transcript_api import YouTubeTranscriptApi
import openai
url="UF8uR6Z6KLc?si=SNmC40_NUn0DjgpI"
a=YouTubeTranscriptApi.get_transcript(url)
c=""
for i in range(len(a)):
    b=a[i]
    c=c+b['text']+" "
# print(c)
    
# Set your OpenAI API key
openai.api_key = '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'
language="English"
def prompt(language,text,num_words):
    return "please summarize this text "+text+"in "+str(num_words)+" words" 
response = openai.Completion.create(
    model="gpt-3.5-turbo-instruct",
    prompt=prompt(language,c,250),
    max_tokens=250,  
)
print(response)
summary = response.choices[0].text

# print("Original Content:\n", content_to_summarize)

print("\nSummary:\n", summary)
