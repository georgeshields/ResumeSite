# George Shields' Resume 

***LINK TO VIEW PROJECT HERE:***
https://georgeshields.github.io/ResumeSite/

This webpage will serve as a more detailed version of my resume. It contains more information than what is given in my PDF file that I submit to employers. I decided to make this because I wanted to be able to add more information about me that might interest potential employers and so that I can give recruiters/hiring managers an opportunity to reach out to me directly through this webpage if they desire. 

So far the project just consists of an index.html file and a projects.html file. Will soon update the project with js files and/or react files for making the site more dynamic. Still drawing/designing the UI at the moment.

Please feel free to use this project as a template for you own personal website. Make sure to acquire your own api key and to never share it. 

# AI Chatbot Feature
As of January 2025, I have written some functionality to allow users to chat with an LLM that can answer questions on my behalf regarding my experience, education, and skills. I am currently using the OpenAI API (using the chatgpt-3.5-turbo model) to help make this feature happen, and I am hoping at some point I can use a custom LLM in its place in the future (likely using deepseek r1). So far i have a brief message in the system content that describes who I am and my experiences. This page also supports darkmode.

# How to Use OpenAI API 
Ensure python3 and flask are installed and that you keep your openai api key safe. Obtain an API key from your openai account and make sure not to share it with anyone (since im testing this project locally I use the <code>export OPENAI_API_KEY='this is where you paste your key'</code> command while in the project directory). Run <code>python3 server.py</code> and open the url in your browser to access locally. Only run the server.py program not the js files.

# Plans to Migrate to Deepseek R1
Updates coming soon.