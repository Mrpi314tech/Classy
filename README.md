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

## API

Go to http://chat.mrpi314.com/api to learn about how to use the api.


## I need more training data

Open a pull request if you have some and put it in unorganized data. I will format it. If you have organized data, put it directly in the intents.json file.

An easy way to contribute is by scrolling through your ChatGPT conversations/Google searches/DALL-E inputs and pasting some of your own data into the unformatted data file.
# Deployed here:
http://chat.mrpi314.com

Charges $0.04 for every image you generate with your api key. Text generation is $0.15 for 1M input tokens (almost nothing).

I can add a custom password for you on the website if you add training data. Message me at 123scoring@gmail.com. Put in the description of the pull request that you want a custom password for your Openai key. 


## Thanks
Thanks to [Patrick Loeber](https://github.com/patrickloeber) for teaching me PyTorch
