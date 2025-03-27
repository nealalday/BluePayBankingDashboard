 # BluePay Banking Performance Dashboard
![Banking_Dashboard1](https://github.com/user-attachments/assets/f9842144-86d9-4fb4-96d0-4e43ffb9e939)
>*Main landing page showing transactions, showing all industries filtered by past fy*

[Link to Tableau Public Dashboard](https://public.tableau.com/app/profile/neal.alday/viz/BluePayBankingPerformanceDashboard/BankingDashboardTransactions)
## Project Background
  As a data analyst for **BluePay**, a full-service banking company based in Melbourne, Australia, I developed a comprehensive dashboard designed to provide key stakeholders with an at-a-glance view of essential Key Performance Indicators (KPIs). This dashboard serves as a central hub for multiple departments, enabling decision-making and performance optimization powered by data.

  The dashboard is structured into three core categories: Transactions, Users, and Cards, with each section offering in-depth metrics and drill-down capabilities tailored for diverse business needs. These include industry performance evaluation, spending pattern analysis, customer financial insights, and business intelligence forecasting.

  The primary objective of this system is to deliver real-time insights into BluePay’s banking operations while maintaining an intuitive and user-friendly interface. By analyzing transaction volumes and values, credit card usage trends, and customer profiles, this dashboard empowers teams to refine strategies, enhance customer engagement, and propel business growth.
  
## Dashboard Pages
![Banking_Dashboard3](https://github.com/user-attachments/assets/1fb8e8ae-f8bc-4fd1-a9e5-acedc89248cc)
>*Customer Information view, filtered by industry; betting industry currently selected*

![Banking_Dashboard_31](https://github.com/user-attachments/assets/7a4880c7-cccb-4164-9c63-d2adef7f64a5)
>*Card Information view, showing all industries in the past fy*

**Global Filters**

<img height="285" alt="Banking_Dashboard11" src="https://github.com/user-attachments/assets/e38060a3-b9a9-487e-bc06-9e468d8181f5" />
<img width="200" alt="Banking_Dashboard12" src="https://github.com/user-attachments/assets/985de1f8-cef8-40b4-a404-0925de2f06d7" />

>*Filter by date and industry*

## Executive Summary
  As of today, **BluePay’s overall transaction volume and value across all industries remain consistent with historical performance from the previous year.** The bank has recorded 8% growth in the number of transactions and a 0.11% increase in total transaction value, with an **upward trend projected over the next 20 months**.

  BluePay currently serves **1.2K+ unique users**, a figure aligned with previous fiscal years. The majority of customers maintain a strong average credit score (700+), while transaction growth is primarily driven by clients in the $15K–$20K credit bracket. Tenured customers have maintained steady spending patterns, whereas **new customers are contributing to a gradual upward trend in transaction volume**. In terms of payment preferences, **Mastercard leads the market** with over 50% share, while **debit cards dominate** as the preferred payment type (70%+ usage). **Online transactions** continue to outperform all other channels, surpassing in-person purchases by as much as **80% across various industries**. 
  
  While individual industries experience periodic fluctuations, **BluePay remains in a strong financial position, with stable transaction movement and continued growth opportunities.**

## Insights Deep-Dive
**Transactions and Industry Analysis**

<img width="688" alt="Banking_Dashboard13" src="https://github.com/user-attachments/assets/2ddbd63f-8331-4757-9177-64e5234ae735" />

- From the beginning of the financial year (FY) to the most recent recorded date, **total transaction volume has increased by 7.9% across all industries** compared to the same period last year. While transaction value has declined by 1%, this variation is largely driven by industry-specific shifts in customer spending patterns rather than an overall downturn.
- **Groceries and Supermarkets lead in both transaction volume and revenue,** generating 3.8 trillion transactions and $4M in revenue over the past 12 months.
- Money Transfers account for the highest financial movement; however, due to the ambiguous nature of these transactions, they are **considered an outlier** rather than a true industry benchmark.
  
| High value, mid-low volume  | High volume, mid-low value |
| ------------- | ------------- |
| Drug stores, pharmaceuticals  | Miscellaneous Food Stores |
| Utilities (electric, gas, etc) | Restaurants |
| Telecommunication services | Service stations |
| Department stores | Wholesale clubs |
| Insurance sales | Toll and bridge fees |

- **Online transactions significantly dwarf in-person purchases across all industries and time periods.** However, certain businesses—such as betting (lotteries, casinos) and beauty services—continue to see higher engagement in physical locations.
- **For industry-specific analysis,** such as for cruise lines and airlines which experience fluctuations in volume and value depending on seasonality, it is best to **gather requirements on which aspects can be further explored and elaborated.**

**Customers**

<img width="400" alt="Banking_Dashboard21" src="https://github.com/user-attachments/assets/c08a9dfa-ff1f-4c2c-9335-ed1f7ea05d73" />
<img width="405" alt="Banking_Dashboard22" src="https://github.com/user-attachments/assets/f643d81a-6cff-4d31-9f53-f015430c7fa3" />

>*Showing Betting industry with the past 12 months date filter*

- **Further analysis on customer segmentation and acquisition patterns can be extracted from the Transactions by Age and Gender data visual**, using the betting industry as an example:
  - Men aged 45-54 show a higher propensity to bet more frequently, but men aged 65+ have bets which are larger in value.
  - Targeting younger demographics (ages 24-34) could present an opportunity for revenue growth.
  - This type of analysis can be applied to virtually any industry for a more comprehensive look on which customer demographics can be harnessed for targeted campaign strategies in the future.
 
<img width="400" alt="Banking_Dashboard23" src="https://github.com/user-attachments/assets/8295d4f3-dfc9-4ee9-9017-c832dff5e9f2" />
<img width="400" alt="Banking_Dashboard28" src="https://github.com/user-attachments/assets/b4442909-4e72-4be8-bd0f-b433d3939b30" />
<img width="184" alt="Banking_Dashboard24" src="https://github.com/user-attachments/assets/e72570a0-8d90-4d1f-8fe3-fed56e699f63" />

>*Visualisation can be filtered according to the length of customer tenure or income group category*

- **Transaction growth is largely pushed by new clients** who have been with BluePay for 12 to 18 months, while tenured customers (5+ years) continue to account for the majority of transaction volume. However, this is largely due to the size of this customer cohort.
  
<img width="473" alt="Banking_Dashboard48" src="https://github.com/user-attachments/assets/257aa735-33d7-44fc-8aa0-c67221bb38b9" />
<img width="450" alt="Banking_Dashboard34" src="https://github.com/user-attachments/assets/d3b0369a-6eb8-4f0a-90f5-310a25398a82" />

- Although online purchases remain the dominant transaction method, but for in-person purchases, the top cities by transaction volume are **Houston, Miami, Brooklyn, Los Angeles, and Chicago.**
- The highest number of transactions comes from residents who live in **Los Angeles, Dallas, Charlotte, Phoenix, and Chicago.**
- **Credit scores remain strong,** with most customers falling within the “Good” range (670-739) and fewer than 10% having a poor score (<580).

**Card Information**

<img width="555" alt="Banking_Dashboard49" src="https://github.com/user-attachments/assets/958e5c43-6813-424b-bfbb-fbeaf482c209" />
<img width="350" alt="Banking_Dashboard50" src="https://github.com/user-attachments/assets/69b91c7d-ff18-47df-a36b-060f0d1a9869" />

- **Debit cards remain the dominant payment method,** accounting for 55%+ of all transactions, followed by credit cards (35%+), while prepaid cards make up the remainder.
- In terms of card brands, **Mastercard holds the largest market share (50%),** followed by Visa (~45%), with Amex and Discover collectively making up less than 20%.
- The volume of issued cards has remained stable over the past decade, with debit cards being the most frequently issued. This aligns with **their continued dominance** as the preferred transaction method.
- Customers with a credit limit of $15K–$20K consistently show the **highest spending behavior across all groups**, a trend observed over the past ten years. This indicates that mid-to-high credit limit users are key revenue drivers.
- Fraud trends remain consistent with previous years, with cases peaking in November, likely due to the holiday shopping season. This seasonal pattern suggests **an opportunity for proactive fraud prevention measures during peak transaction periods.**

## Recommendations
**1. Strengthen Customer Retention & Nurture New Clients**
- **New customers (12–18 months tenure) are driving the highest transaction growth**, both in volume and value. This trend is observed across all payment channels, highlighting the importance of early engagement strategies to maximize customer lifetime value.
- **Develop targeted retention campaigns**, such as personalized offers, cashback incentives, and tiered loyalty programs, to keep these high-growth users engaged.

**2. Enhance & Optimize Online Transactions**
- Online transactions dominate across industries and continue to expand, presenting an opportunity to **further enhance digital banking solutions**.
- **Streamline the online payment experience** with faster checkout processes, seamless integration with e-commerce platforms, and enhanced security measures to maintain trust.
- **Encourage younger customers (ages 18–34) to remain with BluePay** by refining digital banking services, including better mobile app UX, budgeting tools, and AI-driven financial insights.

**3. Leverage Promotions for In-Person Transactions**
- While digital transactions lead overall, brick-and-mortar industries like grocery stores, supermarkets, and beauty services still **generate significant in-person purchases**.
- Offer industry-specific promotions, such as cashback for grocery spending, salon service discounts, or fuel rewards, to increase spending in these sectors.

**4. Increase Credit Card Issuance for Higher Revenue Potential**
-**Credit cards offer higher returns** on assets and greater merchant discount rate revenue compared to debit transactions.
- **Target high-spending customer segments ($15K–$20K credit limit users)** with exclusive benefits, such as increased rewards, travel perks, or reduced annual fees, to encourage greater credit card adoption.

**5. Strengthen Partnerships with Mastercard**
- With Mastercard holding the highest transaction share (50%), **exploring co-branded partnerships can drive further engagement**.
Potential initiatives include:
  - Merchant-specific rewards (e.g., exclusive discounts for Mastercard users at partner retailers).
  - Cashback or points-based loyalty programs to encourage repeat spending.
  - Co-branded promotional campaigns to reinforce brand loyalty and increase card usage.

By implementing these strategic recommendations, **BluePay can power sustained growth, improve customer engagement, and maximize revenue opportunities in both digital and in-person transaction spaces.**

## Dashboard Details

<img width="629" alt="Banking_Dashboard4" src="https://github.com/user-attachments/assets/218e11e3-d581-498d-9b21-9d8dad8c8499" />

>*Dynamic KPIs that update depending on date and industry filters*

<img width="350" alt="Banking_Dashboard20" src="https://github.com/user-attachments/assets/32fab513-5f41-4f94-93e3-bfe040edde52" />
<img width="252" alt="Banking_Dashboard47" src="https://github.com/user-attachments/assets/6cfb4011-b703-4497-9211-aa27fd28e6e7" />
<img height="150" alt="Banking_Dashboard45" src="https://github.com/user-attachments/assets/402e3803-e7ba-49b2-a6b5-9a9e868d7ba2" />

>*Tooltips that show additional details*

## Dataset ERD
![BluePay_ERD](https://github.com/user-attachments/assets/17ccb746-65f2-42a9-b042-58005ec31ec0)
>*BluePay Dataset ERD*
