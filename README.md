# Classy
## How to use
Install: 
<pre><code>pip install Classy-AI</code></pre>
Setup:
<pre><code>import Classy
Classy.download()</code></pre>
Downloads "data.pth" to your working directory. Also downloads the NLTK "punkt" tokenizer

Usage (Pre built with OpenAI and other tools):
<pre><code>import Classy
Classy.init('/path/to/data.pth','OpenAI api key')
primary, secondary, stemmed, organized = Classy.question("hello, how are you?")</code></pre>
Usage (Just the classifier)
<pre><code>import Classy
Classy.init('/path/to/data.pth','Nothing here')
intent, certainty = Classy.classify("hello, how are you?")</code></pre>

## I need more training data

Open a pull request if you have some and put it in unorganized data. I will format it. If you have organized data, put it directly in the intents.json file
# Deployed here:
http://chat.mrpi314.com

Website only works if one person is using it

Charges $0.04 for every image you generate with your api key. Text generation is $0.50 for 1M input tokens (almost nothing).

I can add a custom password for you on the website if you add training data. Message me at 123scoring@gmail.com. Put in the description of the pull request that you want a custom password for your Openai key. 
