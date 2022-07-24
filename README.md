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
 <li>Install Requirements.txt</li>
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

 
 
    


