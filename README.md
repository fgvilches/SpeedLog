<a href="https://twitter.com/fgvilches"><img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/fgvilches?style=social"></a>
<a href="https://github.com/fgvilches"><img alt="GitHub followers" src="https://img.shields.io/github/followers/fgvilches?style=social"></a>

# SpeedLog
Simple code to make Speed tests and save the results to csv's that i've made for a client last month.

### Requirements
  - Python 3
  - speedtest-cli lib
 
### Just run the code and the speedtest starts with Entel Chile ISP.

If you need to change isp server list you can edit the "server_mimize.json" file and "server.json" files dependending on what mode you need to execute.

This lines:
<div align="left">
  <img src="/Screenshots/SS1.PNG" alt="Line" width="60%">
</div>
Modify the type of test you are gonna realize (multi or single) and the json file you are gonna utilize (minimize or server) dependeding on the type of analysis.

### Results
The results csv are obtained in this format "results_+ date + .csv".

Thanks to the use of the time library, a new file is generated every day.

This is the format of the results csv file:
<div align="left">
  <br>
  <img src="/Screenshots/SS2.PNG" alt="Line" width="70%">
  </br>
</div>


The tests are performed every 15 minutes, you can modify this in the following lines
<div align="left">
  <img src="/Screenshots/SS3.PNG" alt="Line" width="35%">
</div>
<div align="left">
  <img src="/Screenshots/SS4.PNG" alt="Line" width="50%">
</div>
