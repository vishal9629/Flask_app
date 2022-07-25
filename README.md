<h1>Web-App login using Github</h1>
<p><b>In this project we used OAUTH to login with Github.</b></p>
<hr border-top: 1px dashed>
<h2>Requirements</h2>
<ul type ="disc">
<li>python 3.10.5</li>
 <li>Flask</li>
  <li>git</li>
</ul>
<hr>
<h2>How to setup</h2>
<ul type="disc">
 <li>Install python</li>
 <li>Clone this reporistory.</li>
 <li>Navigate to this directory.</li>
 <li>Create a virtual enviornment for project.</li>
 <li>Activate the virtualenv.</li>
 <li>Install requirements.txt</li>
 <li>Open your github account</li>
 <li>Go to Settings/Developer settings.</li>
 <li>Select OAuth apps and click on New OAuth app.</li>
 <li>Fill all the details.</li>
 <li>For Homepage URL fill http://127.0.0.1:5000/</li>
 <li>For Authorization callback URL fill http://127.0.0.1:5000/login/github/authorize</li>
 <li>Click on Register Application</li>
 <li>Now you will have Client id.</li>
 <li>Genrate Client Secret.</li>
 <li>Paste your Client ID and Client Secret in .env.</li>
 </ul>
<h3>Run the code</h3>
<ul type="disc">
 <li>Check your vitualenv is activated.</li>
 <li>To start the app type Python app.py.</li>
 <li>Click on link genrated in terminal.</li>
 </ul>
<hr>
<h2>Problem Statement</h2>
 Create a very simple web app with Flask Backend. There should be two pages to it:
 <ul>
<li> Login Page: To login via GitHub.</li>
<li> After login, display the user's name and image.</li>
<li> Write a GitHub Action workflow file with Cirun to set up the app in the CI.</li>
 </ul>
<hr>
<h2>Approach to the problem</h2>
<ul type="disc">
<li>I divided the task into 2 parts.</li>
<li>For the first one it was log in with Github.</li>
<li>Then I created an OAuth registry and routes for Github OAuth.</li>
<li>Registering your OAuth app with Github and creating Client_id and Client_secret.</li>
<li>Then I returned my app to the authorized page.</li>
<li>Then I fetch the user name and profile from JSON file.</li>
<li>I displayed it on returned page.</li>
<br>
<li>In the second one it is for Writing a Github Action workflow file with Cirun to set up the app in the CI.</li>
<li>For this, I read the documentation of Github action workflow.</li>
<li>Then I write a Github action workflow file.</li>
<li>I tested it and it's working fine.</li>
<li>Then a wrote a self hosted Github action workflow file.</li>
<li>I set up the runner on my pc and tested it.</li>
<li>To set up it with Cirun, I read the documentation.</li>
<li>Then I wrote a .cirun.yml.</li>
<li>I install Cirun on my Github and gave access to this repo.</li>
<li>I connected my Digitalocean with Cirun.</li>
<li>I commit an update on my repo and the runner is running fine.</li>
</ul>
<hr>
<h2>Difficulties faced</h2>
<ul type="disc">
<li>I faced my first difficulty when I tried to fetch profile photo and name after authorizing with Github.</li>
<li>I tried to find this on google but nothing was found about this.</li>
<li>In OAuth documentation found on authentication it will return with JSON file in which it contains all details.</li>
<li>Then I was able to fetch the user name and profile link.</li>
<li>My second difficulty came when I tried to run my actions on self-hosted runner.</li>
<li>But I fixed it.</li>
</ul>
<hr>
<h2>Video demo</h2>
<ul>
<!-- <li>Youtube link - https://youtu.be/Od2RBSkRPec</li> -->
</ul>


 
 
    


