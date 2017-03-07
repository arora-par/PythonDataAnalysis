### Introduction
Enron was the world's major energy company found in 1985 based out of Houston, Texas. It was named the most innovative company by Forbes for six consecutive years and claimed revenue in hundreds of billions during the year 2000 before it went bankrupt in Oct 2001. Enron was involved in a systematically planned accounting fraud, the Enron Scandal, hiding the company's financial condition. The bankruptcy case filed by the company is known to be one of the most complex bankruptcy cases in the US history. The Enron dataset consists of half a million emails of its employees.

### Goal
The goal of this analysis is to identify and uncover people related to the scandal using the email dataset and communication patterns therein.

### Approach
The major chunk of the emails provided in the dataset is of the period 1998 to 2002. So, I divided this duration into 3 stages:
- 1998 to 14th Aug 2001 (when the second CEO Jeff Skilling resigned suddenly)
- 15th Aug to 2nd Dec (period between Jeff's resignation and when Enron scandal was out and company filed for bankruptcy)
- 3rd Dec to 31st Dec 2002 (when the employees were supporting their company while media was beating down Enron by questioning it)

### Conclusion
- Looking at how closely their involvement matches up across the first 2 stages, there is no doubt that Jeff Skilling must have had access to insider information even after his resignation.
- There are different people involved in different stages in both Kenneth Lay's and Jeff Skilling's emails. This means that while the 'trio' gained the most from the scandal, there were a lot more people that must have helped them with the Fraudulent Financial Accounting during Stage 1 and later Insider Trading during Stage 2. 
- As it is evident from some of the email ids, the government agencies (GHCF) and media (CNN) started questioning the resignation of Jeff Skilling and they continued to question them after the Bankruptcy. There was something wrong before and after Jeff Skilling was CEO and the media had got the attention.
- Looking at the word clouds of conversations between the trio and other important people, the following conclusions can be drawn:
    - 1. Stage 1 -> 'ECT' -> There was a lot of push towards shifting towards transitioning towards a energy-trade platform rather than stay the course of energy supplier.
    - 2. Stage 2 - 'Derivatives', 'Stock' - There was a lot of talk around financial trading, which hints at Insider Trading. 
    - 3. Stage 3 -> 'CNN', 'Love', 'God', 'Pray', 'Heart' - Enron was beaten down by media and the government. But the employees continued supporting the company with 'love' and 'heart'.
- In addition, there are a lot of names - of people and places - that should be investigated next.
