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
 <li>For Homepage URL fill http://localhost:5000</li>
 <li>For Authorization callback URL fill http://localhost:5000/api/auth/github</li>
 <li>Click on Register Application</li>
 <li>Now you will have Client id.</li>
 <li>Genrate Client Secret.</li>
 <li>Paste your Client ID and Client Secret in .env.</li>
 <ul>
<h2>Run the code</h2>
<ul type="disc">
 <li>Check your vitualenv is activated.</li>
 <li>To start the app type Python Flask_app.</li>
 <li>Click on link genrated in terminal.</li>
 
    


