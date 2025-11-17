# Assignment for Research and Development / AI

## Basic Assignment Rules

### Academic Integrity



- **Proper Citation:** When referencing external sources, ideas, or quotes, students must provide appropriate citations following the required citation style (APA, MLA, Chicago, etc.).

### 

### Problem

Find the values of unknown variables in the given parametric equation of a curve :

$$
x=\left(t*\cos(\theta)-e^{M\left|t\right|}\cdot\sin(0.3t)\sin(\theta)\ +X \right )
$$

$$
y = \left (42 + t*\sin(\theta)+e^{M\left|t\right|}\cdot\sin(0.3t)\cos(\theta)\right)
$$

unknowns are 

$$
\theta , M ,X
$$

Given range for unknown params is :

$$
0 \deg<\theta<50 \deg \\
-0.05<M<0.05 \\
0<X<100\\
$$

parameter ‘t’ has range:

$$
6<t<60
$$

### Given is the list of points that lie on the curve for  $6<t<60$ :

[xy_data.csv](attachment:abeca04b-e68f-4a68-8322-b75a272bef33:xy_data.csv)

### Assessment Criteria:

The candidates will be judged on following:

- The L1 distance between uniformly sampled points between expected and predicted curve (max score 100)
- Explanation on complete process and steps followed (max score 80)
- Submitted code / github repo (max score 50)
- *Note: Even if your answer is incorrect or incomplete, you will receive credit for explaining your thought process and approach.*

Submission Format

- For the following assignment the only required and necessary result is the value of **Unknown variables** ,  submission can be made by writing and copying equations in latex format or from the following website in the readme file of the submitted github repo: https://www.desmos.com/calculator/rfj91yrxob
- Example submission : 
”\left(t*\cos(0.826)-e^{0.0742\left|t\right|}\cdot\sin(0.3t)\sin(0.826)\ +11.5793,42+\ t*\sin(0.826)+e^{0.0742\left|t\right|}\cdot\sin(0.3t)\cos(0.826)\right)”
translates to :

![image.png](attachment:681a6024-98f6-481f-b061-425115f2e88a:image.png)

- Additional code / maths used to estimate / extract the variables will be a plus