<h1 class="AnswerParser_AnswerParserH1__6UNv6"><strong>Premier Rating Grabber</strong></h1>
<p><span class="AnswerParser_TextContainer__z_Iiv" data-testid="youchat-text">The&nbsp;<strong>Premier Rating Grabber</strong>&nbsp;is a Python-based tool designed to extract, track, and visualize player ratings from online profiles. It automates the process of fetching player ratings from a specified URL, saving the data to a CSV file, and generating a graph to display rating trends over time.</span></p>
<hr />
<h2 class="AnswerParser_AnswerParserH2__SIHnF"><strong>Features</strong></h2>
<ul class="AnswerParser_AnswerParserUnorderedList__P_1FW">
<li class="AnswerParser_ListItem__XqLOV" translate="yes">Automatically fetches player ratings from&nbsp;<a class="sc-dbab3f55-0 VWGXo" href="https://leetify.com/" data-eventactiontitle="Open Anchor Link">Leetify</a>&nbsp;every 30 minutes.</li>
<li class="AnswerParser_ListItem__XqLOV" translate="yes">Saves ratings with timestamps to a CSV file for historical tracking.</li>
<li class="AnswerParser_ListItem__XqLOV" translate="yes">Generates a graph to visualize rating trends over time.</li>
<li class="AnswerParser_ListItem__XqLOV" translate="yes">Updates a text file for seamless integration with Streamlabs Desktop overlays.(SOON)</li>
<li class="AnswerParser_ListItem__XqLOV" translate="yes">Provides a customizable HTML overlay (<code translate="no">Rating.html</code>) for live streaming with CS2 Premier Rating.</li>
</ul>
<hr />
<h2 class="AnswerParser_AnswerParserH2__SIHnF"><strong>How to Use</strong></h2>
<ol class="AnswerParser_AnswerParserOrderedList__kl_2Y">
<li class="AnswerParser_ListItem__XqLOV" translate="yes"><span class="AnswerParser_TextContainer__z_Iiv" data-testid="youchat-text"><strong>Set the Player URL</strong>:<br />Navigate to&nbsp;<code translate="no">https://leetify.com/app/profile/GRAB_YOUR_ID_AND_PASTE_IT_HERE</code>&nbsp;and replace the placeholder with your player ID.</span></li>
<li class="AnswerParser_ListItem__XqLOV" translate="yes"><span class="AnswerParser_TextContainer__z_Iiv" data-testid="youchat-text"><strong>Future Updates</strong>:</span>
<ul class="AnswerParser_AnswerParserUnorderedList__P_1FW">
<li class="AnswerParser_ListItem__XqLOV" translate="yes"><strong>CSSTATS Integration</strong>: Future updates will include support for CSSTATS data.</li>
<li class="AnswerParser_ListItem__XqLOV" translate="yes"><strong>Premier Rank Colors</strong>: To seamlessly change the premier rank between colors as your rank up live. Currently, you will need to obtain the static image from CSStats in Inspect Element for each ELO. I've attached local .png for convenience if you want to host it yourself.</li>
</ul>
<span class="AnswerParser_TextContainer__z_Iiv" data-testid="youchat-text"><span class="AnswerParser_TextContainer__z_Iiv" data-testid="youchat-text">CSStats Inspect Element:<br /></span></span>
<div class="ChatImage_ImageContainer__Cx_sd">
<div class="sc-bbbfc4a4-0 cSXvlq">
<div class="sc-bbbfc4a4-1 fLunLb"><img class="sc-bbbfc4a4-4 eUaIut" src="https://github.com/user-attachments/assets/04b87963-f10f-4913-aa08-ee1394332af1" alt="" /></div>
</div>
</div>
</li>
<li class="AnswerParser_ListItem__XqLOV" translate="yes"><span class="AnswerParser_TextContainer__z_Iiv" data-testid="youchat-text"><strong>Streamlabs Integration</strong>:<br />Use the&nbsp;<code translate="no">Rating.html</code>&nbsp;file as a custom widget in Streamlabs Desktop. For now, you will need to manually edit your rating, but future updates will automate this process.</span></li>
</ol>
<hr />
<h2 class="AnswerParser_AnswerParserH2__SIHnF"><strong>Dependencies</strong></h2>
<p><span class="AnswerParser_TextContainer__z_Iiv" data-testid="youchat-text">This tool requires the following dependencies to be installed:</span></p>
<h3 class="AnswerParser_AnswerParserH3__Mpe4s"><strong>1. Python 3.8+</strong></h3>
<ul class="AnswerParser_AnswerParserUnorderedList__P_1FW">
<li class="AnswerParser_ListItem__XqLOV" translate="yes">Ensure you have Python installed on your system. You can download it from&nbsp;<a class="sc-dbab3f55-0 VWGXo" href="https://www.python.org/" data-eventactiontitle="Open Anchor Link">python.org</a>.</li>
</ul>
<h3 class="AnswerParser_AnswerParserH3__Mpe4s"><strong>2. Required Python Libraries</strong></h3>
<p><span class="AnswerParser_TextContainer__z_Iiv" data-testid="youchat-text">The following Python libraries are required for the tool to function:</span></p>
<ul class="AnswerParser_AnswerParserUnorderedList__P_1FW">
<li class="AnswerParser_ListItem__XqLOV" translate="yes"><code translate="no">selenium</code>&nbsp;- For web scraping and browser automation.</li>
<li class="AnswerParser_ListItem__XqLOV" translate="yes"><code translate="no">matplotlib</code>&nbsp;- For generating graphs.</li>
<li class="AnswerParser_ListItem__XqLOV" translate="yes"><code translate="no">schedule</code>&nbsp;- For scheduling tasks to run periodically.</li>
<li class="AnswerParser_ListItem__XqLOV" translate="yes"><code translate="no">time</code>&nbsp;- For managing delays in the script.</li>
<li class="AnswerParser_ListItem__XqLOV" translate="yes"><code translate="no">csv</code>&nbsp;- For handling CSV file operations.</li>
<li class="AnswerParser_ListItem__XqLOV" translate="yes"><code translate="no">os</code>&nbsp;- For file path and directory management.</li>
<li class="AnswerParser_ListItem__XqLOV" translate="yes"><code translate="no">datetime</code>&nbsp;- For working with timestamps.</li>
</ul>
<h3 class="AnswerParser_AnswerParserH3__Mpe4s"><strong>3. Google Chrome</strong></h3>
<ul class="AnswerParser_AnswerParserUnorderedList__P_1FW">
<li class="AnswerParser_ListItem__XqLOV" translate="yes">The tool uses Google Chrome for browser automation. Ensure you have the latest version of Chrome installed.</li>
</ul>
<h3 class="AnswerParser_AnswerParserH3__Mpe4s"><strong>4. ChromeDriver</strong></h3>
<ul class="AnswerParser_AnswerParserUnorderedList__P_1FW">
<li class="AnswerParser_ListItem__XqLOV" translate="yes">ChromeDriver is required to control the Chrome browser. Download the version of ChromeDriver that matches your Chrome browser version from&nbsp;<a class="sc-dbab3f55-0 VWGXo" href="https://chromedriver.chromium.org/downloads" data-eventactiontitle="Open Anchor Link">ChromeDriver Downloads</a>.</li>
</ul>
<h3 class="AnswerParser_AnswerParserH3__Mpe4s"><strong>5. Code Editor (Optional)</strong></h3>
<ul class="AnswerParser_AnswerParserUnorderedList__P_1FW">
<li class="AnswerParser_ListItem__XqLOV" translate="yes">For editing and running the code, you can use&nbsp;<strong>VSCodium</strong>&nbsp;(an open-source alternative to Visual Studio Code) or other alternatives like:
<ul class="AnswerParser_AnswerParserUnorderedList__P_1FW">
<li class="AnswerParser_ListItem__XqLOV" translate="yes"><strong>Notepad++</strong></li>
<li class="AnswerParser_ListItem__XqLOV" translate="yes"><strong>Sublime Text</strong></li>
<li class="AnswerParser_ListItem__XqLOV" translate="yes"><strong>PyCharm</strong></li>
<li class="AnswerParser_ListItem__XqLOV" translate="yes"><strong>Atom</strong></li>
</ul>
</li>
</ul>
<hr />
<h2 class="AnswerParser_AnswerParserH2__SIHnF"><strong>Installation Instructions</strong></h2>
<p><span class="AnswerParser_TextContainer__z_Iiv" data-testid="youchat-text">To install all the required Python libraries, you can use the provided&nbsp;<code translate="no">install.bat</code>&nbsp;file. This will automatically install the dependencies using&nbsp;<code translate="no">pip</code>.</span></p>
<h3 class="AnswerParser_AnswerParserH3__Mpe4s"><strong>Install.bat File</strong></h3>
<p><span class="AnswerParser_TextContainer__z_Iiv" data-testid="youchat-text">The&nbsp;<code translate="no">install.bat</code>&nbsp;file contains the following commands:</span></p>
<div translate="no">
<div data-testid="youchat-code">
<div class="rabwn52">
<div class="rabwn56">bat</div>
<div class="rabwn53">&nbsp;</div>
</div>
<div class="code-block rabwn50">
<pre class="hljs"><code class="language-cpp"><span class=""><span class="">@echo off
</span></span><span class="">echo Installing required Python libraries...
</span><span class="">pip install selenium
</span><span class="">pip install matplotlib
</span><span class="">pip install schedule
</span><span class="">echo All dependencies have been installed successfully!
</span><span class="">pause
</span></code></pre>
</div>
</div>
</div>
<h3 class="AnswerParser_AnswerParserH3__Mpe4s"><strong>How to Use the Install.bat File</strong></h3>
<ol class="AnswerParser_AnswerParserOrderedList__kl_2Y">
<li class="AnswerParser_ListItem__XqLOV" translate="yes">Save the above content into a file named&nbsp;<code translate="no">install.bat</code>&nbsp;in the root directory of your project.</li>
<li class="AnswerParser_ListItem__XqLOV" translate="yes">Double-click the&nbsp;<code translate="no">install.bat</code>&nbsp;file to run it.</li>
<li class="AnswerParser_ListItem__XqLOV" translate="yes">The script will automatically install all the required Python libraries.</li>
</ol>
<hr />
<h2 class="AnswerParser_AnswerParserH2__SIHnF"><strong>How It Works</strong></h2>
<ul class="AnswerParser_AnswerParserUnorderedList__P_1FW">
<li class="AnswerParser_ListItem__XqLOV" translate="yes">The tool fetches new data every 30 minutes to allow for real-time updates to your rating while you stream.</li>
<li class="AnswerParser_ListItem__XqLOV" translate="yes">To cancel the process, simply press&nbsp;<code translate="no">Ctrl+C</code>&nbsp;in the terminal.</li>
</ul>
<hr />
<h2 class="AnswerParser_AnswerParserH2__SIHnF"><strong>Overlay Example</strong></h2>
<p><span class="AnswerParser_TextContainer__z_Iiv" data-testid="youchat-text">Here&rsquo;s an example of the overlay you can use with Streamlabs Desktop:</span></p>
<div class="ChatImage_ImageContainer__Cx_sd">
<div class="sc-bbbfc4a4-0 cSXvlq">
<div class="sc-bbbfc4a4-1 fLunLb"><img class="sc-bbbfc4a4-4 eUaIut" src="https://github.com/user-attachments/assets/92842412-ecfd-4026-b670-7d866fc1a73f" alt="" /></div>
</div>
</div>
<hr />
<h2 class="AnswerParser_AnswerParserH2__SIHnF"><strong>Additional Notes</strong></h2>
<ul class="AnswerParser_AnswerParserUnorderedList__P_1FW">
<li class="AnswerParser_ListItem__XqLOV" translate="yes">Ensure that&nbsp;<code translate="no">pip</code>&nbsp;is added to your system's PATH environment variable. If&nbsp;<code translate="no">pip</code>&nbsp;is not recognized, you may need to reinstall Python and check the option to add it to PATH during installation.</li>
<li class="AnswerParser_ListItem__XqLOV" translate="yes">If you encounter any issues with ChromeDriver, ensure that the version matches your installed Chrome browser version.</li>
</ul>
<hr />
<h2 class="AnswerParser_AnswerParserH2__SIHnF"><strong>Enjoy the Tool!</strong></h2>
<p><span class="AnswerParser_TextContainer__z_Iiv" data-testid="youchat-text">Created by&nbsp;<strong>Spoon</strong>.<br />Feel free to contribute or suggest improvements!</span></p>
