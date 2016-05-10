<p><strong>About my project:</strong></p> 
<p>I scraped the results of Columbia restaurants' safety inspections from the Columbia/Boone County Public Health and Human Services’ website. (The link is: https://www.gocolumbiamo.com/CMS/health_inspections/) I then used "agate" to analyze my data and used Tableau to map it.</p> 

<p><strong>How I made it:</strong></p> 
<p>1.	I used Python to scrape the data I want from the five restaurant inspection pages separately. I first extracted all the subpages' urls from the root page, and then loop over all the subpages to get the information I want. As I only want the most recent result, instead of using "find_all", I used "find" to get the first set of data. I then used “replace” to replace the content that I don’t need into comma, which makes it easier when I import the .txt file into xlsx.</p>  
<p>2.	After getting the data in my terminal, I put it into a txt.file, and then imported it into xlsx. As the data is very dirty, I went through each row and make sure that there was no repeating data or irrelevant restaurant. I also converted addresses into geocode for mapping the data later.</p>  
<p>3.	I then used agate to analyze my data. According to my analysis, the median critical violation and median non-critical violation of Columbia restaurants is 0, which is pretty good in general. El Tigre, a Mexican restaurant has 9 critical violations, ranking the first in the latest inspection. Among the top 10 restaurants with the most critical violations, 5 are Asian restaurants.</p>  
<p>In terms of non-critical violation, Chinese Wok Express ranked the first with a total of 9 non-critical violations. Surprisingly, Kaldi’s coffee ranked the 5th, which has five non-critical violations.</p> 
<p>I then combined the critical and non-critical violations, and the data suggested that Chinese Wok Express ranked the first again with 14 violations in total. The top five unsafe restaurants consist of four Asian restaurants and one Mexican restaurant.</p> 
<p>4.	Finally, I made a restaurant map by using Tableau, and published it at: https://public.tableau.com/profile/publish/FinalProject_166/Howsafeistherestaurant#!/publish-confirm</p> 


<p><strong>What is the next:</strong></p>  
<p>I am planning to improve the script and to figure out a way to put the data directly into csv. I also wish to use more advanced library to make my map better and more interactive.</p>  