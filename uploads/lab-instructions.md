::page{title="Hands-on Lab: Creating a Simple Web page"}

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-CD0101EN-SkillsNetwork/images/IDSN-logo.png" width="200" alt="cognitiveclass.ai logo">

##

<b>Estimated time:</b> 35 mins

You are a web developer who has been approached by the fan club for IBM founder, **Thomas J. Watson Sr.**, to create a web page for them. 

In this lab, we\'ll create a web page with details of Mr. Watson.

## Objectives

After this exercise, you will be able to do the following:

1. Create a new HTML document 
2. Specify the DOCTYPE
3. Add the head and body elements
4. Add a title
5. Add a heading
6. Add a paragraph
7. Add an image
8. Create a list of items
9. Add a table of data
10. Add links to other pages
11. Add feedback form to collect user input

::page{title="Create a new HTML document"}

Let\'s create mywebpage.html file where we will be typing in our html markup.
On the window to the right, click the **File** menu and select the **New File** option, as shown in the image below.<br>
![myfile.png](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/NsBIScvH38bA28_BiFVEcg/Screenshot%202025-04-30%20131514.png)
A pop up appears with title **New File**, as shown in the image below.<br>
![myhtml.png](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/ggfar0aWztZu7I4HRtfnSw/myhtml.png)
Enter \"mywebpage.html\" as the file name and click **OK**.<br>

A file titled \"mywebpage.html\" will be created for you.Make sure it is created in the \"/home/project\" directory.<br>



Open **mywebpage.html** in IDE as shown below.

Every line of HTML you write from now on will be saved into this file.<br>
![File Name](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-CD0101EN-SkillsNetwork/labs/Theia%20Labs/01%20-%20HTML%20and%20CSS/Lab%201%20HTML/images/new_file_tab.png)<br>
You are now ready to start creating your web page.

::page{title="Specify  <!DOCTYPE>"}

All HTML documents start with the **<!DOCTYPE>** declaration.<br>

This line tells the web browser that the file contains HTML code. This is *not* an HTML tag.<br>

This line is specified as follows:<br>

```html
<!DOCTYPE html>
```

Insert the above code into the HTML file you created in the previous step.<br>

Your file should now look like this:<br>
![File Name](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-CD0101EN-SkillsNetwork/labs/Theia%20Labs/01%20-%20HTML%20and%20CSS/Lab%201%20HTML/images/start_writing_code.png)

::page{title="Add the `<head>` and `<body>` elements"}

Now that we\'ve added the doctype, let\'s begin adding the HTML code.<br>

An HTML file begins with the **`<html>`** tag and ends with the corresponding closing **`</html>`** tag. All HTML code will be placed within these two tags.

The HTML document is divided up into two sections: a *head* and a *body*

The **`<head>`** tag defines the metadata about the page, which is used by browsers and search engines. 
This information may include the document title, character set, styles to be used, scripts, etc. 
Contents of `<head>` section are *not* displayed to the user.

The  **`<body>`** tag defines the document body, and contains all the visible content such as headings, paragraphs, images, links, tables, etc.

The skeleton of an HTML document looks like this:

Add the code below to your file, beneath your doctype declaration.<br>

```html
<html>
<head>
    
</head>
<body>

</body>
</html>
```

::page{title="Add a title"}

The title of the page appears on the browser tab, when you open the webpage in the browser.

The title is defined using the `<title>` tag, which will be added within the `<head>` section.

Now, let us define our webpage using this element.<br>

Add the code below inside the `<head>` section of your document.<br>

```html
<title>Thomas J. Watson Sr -  Fan Page</title>
```

Your code should now look like this:<br>

```html
<!DOCTYPE html>
<html>
<head>
    <title>Thomas J. Watson Sr -  Fan Page</title>
</head>
<body>

</body>
</html>
```

::page{title="Add a heading to the page"}

To add a heading, we will use the `<h1>` tag. This stands for \"heading 1\" and is used to indicate the most important heading. HTML headings go from `<h1>` to `<h6>`, to represent a descending order of importance.<br>

Type the below code in the `<body>` section.<br>

```html
<h1>Thomas J. Watson</h1>
```

Your code should look like this:<br>

```html
<!DOCTYPE html>
<html>
<head>
    <title>Thomas J. Watson Sr - Fan Page</title>
</head>
<body>
    <h1>Thomas J. Watson</h1>
</body>
</html>
```

Go to the **File** menu and click **Save** to save your code.<br>
![File Name](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-CD0101EN-SkillsNetwork/labs/Theia%20Labs/01%20-%20HTML%20and%20CSS/Lab%201%20HTML/images/save_file.png)
<br><br>

::page{title="Preview your HTML File"}

**To preview your file, you can use the built-in Live Server extension by following the instructions below.**

1. Open the file explorer and navigate to your file.
![File Name](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-CD0101EN-SkillsNetwork/labs/Theia%20Labs/01%20-%20HTML%20and%20CSS/Lab%201%20HTML/images/Live_server_0.png)
<br>

2. Right click your file & click \"Open with Live Server\"
![File Name](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-CD0101EN-SkillsNetwork/labs/Theia%20Labs/01%20-%20HTML%20and%20CSS/Lab%201%20HTML/images/Live_server_1.png)
<br>

3. This should show a notification mentioning that the server has started on port 5500.
![File Name](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-CD0101EN-SkillsNetwork/labs/Theia%20Labs/01%20-%20HTML%20and%20CSS/Lab%201%20HTML/images/Live_server_2.png)
<br><br><br>

4. Click \'Launch Application\' button similar to the one below to launch the application or click Skills Network button on the left to open the \"Skills Network Toolbox\". Click \"Other\" and then \"Launch Application\". From there, enter the port number as 5500 and launch your application.

::startApplication{port="5500" display="internal" name="Launch Application" route="/"}

![File Name](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-CD0101EN-SkillsNetwork/labs/Theia%20Labs/01%20-%20HTML%20and%20CSS/Lab%201%20HTML/images/Live_server_3.0.png)

5. Click the file name to view its preview.
![File Name](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-CD0101EN-SkillsNetwork/labs/Theia%20Labs/01%20-%20HTML%20and%20CSS/Lab%201%20HTML/images/Live_server_4.png)

::page{title="Add a Paragraph"}

Now, let\'s add a short description. <br>

The tag `<p>` is used to define a paragraph. <br>

In this example, we\'ll add a few lines about Thomas J. Watson. <br>

Add the below code after the `<h1>` heading .<br>

```html
<p>Thomas J. Watson, Sr. is the American industrialist, who built the International Business Machines Corporation (IBM) into the largest manufacturer of electric typewriters and data-processing equipment in the world.
</p>
```

Your code should look like this now.<br>

```html
<!DOCTYPE html>
<html>
<head>
    <title>Thomas J. Watson Sr - Fan Page</title>
</head>
<body>
    <h1>Thomas J. Watson </h1>
    <p>Thomas J. Watson, Sr. is the American industrialist, who built the International Business Machines Corporation (IBM) into the largest manufacturer of electric typewriters and data-processing equipment in the world.
    </p>
</body>
</html>
```

Go to the **File** menu and click **Save** to save your code.<br>

The resulting web page looks like this.<br>

![Paragraph](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-CD0101EN-SkillsNetwork/labs/Theia%20Labs/01%20-%20HTML%20and%20CSS/Lab%201%20HTML/images/5.png)

::page{title="Add an Image"}

An `<img>` tag is used to add an image.<br>

Let\'s add an image of Thomas J. Watson after the heading. <br>
To add an image you need to know the image file name and mention it in the \'src\' attribute.<br>
The \'src\' attribute specifies an external resource that you want to link, such as the URL of an image.<br>
You can optionally specify how many pixels the width and height of the image should be.<br>
Type the below code after the `<h1>` heading .<br>

```html
<img src="https://upload.wikimedia.org/wikipedia/commons/7/7e/Thomas_J_Watson_Sr.jpg" width="300" height="300">
```

Your code should look like this now.<br>

```html
<!DOCTYPE html>
<html>
<head>
    <title>Thomas J. Watson Sr -  Fan Page</title>
</head>
<body>
    <h1>Thomas J. Watson </h1>
    <img src="https://upload.wikimedia.org/wikipedia/commons/7/7e/Thomas_J_Watson_Sr.jpg" width="300" height="300">
    
    <p>Thomas J. Watson, Sr. is the American industrialist, who built the International Business Machines Corporation (IBM) into the largest manufacturer of electric typewriters and data-processing equipment in the world.
    </p>
</body>
</html>
```

Go to the **File** menu and click **Save** to save your code.<br>

The resulting web page looks like this.<br>
![Image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-CD0101EN-SkillsNetwork/labs/Theia%20Labs/01%20-%20HTML%20and%20CSS/Lab%201%20HTML/images/6.png)

::page{title="Create a List"}

To create a list of items, we can use  the  `<ol>` (ordered list) tag for numbered lists, and the `<ul>` (unordered list) tag for bulleted lists.<br>
Each point within a list will be enlosed by a `<li>` opening and closing tag, which represents a _list item_. This same tag is used for both ordered and unordered list.

Let\'s add a few more lines of information about Mr. Watson after the main paragraph, in the form of a list. <br>

Type the below code after the `<p>` paragraph.<br>

```html
<ul>
    <li>In 1939, he received an honorary degree in Doctor of Commercial Science from Oglethorpe University. </li>
    <li>In 1940s, Watson was on the national executive board of the Boy Scouts of America. </li>
    <li>Watson served as a trustee of Columbia University from June 6, 1933, until his death. </li>
    <li>He was posthumously inducted into the Junior Achievement U.S. Business Hall of Fame in 1990.</li>
</ul>
```

Your code should look like this now.<br>

```html
<!DOCTYPE html>
<html>
<head>
    <title>Thomas J. Watson Sr -  Fan Page</title>
</head>
<body>
    <h1>Thomas J. Watson </h1>
    <img src="https://upload.wikimedia.org/wikipedia/commons/7/7e/Thomas_J_Watson_Sr.jpg" width="300" height="300">
    
    <p>Thomas J. Watson, Sr. is the American industrialist, who built the International Business Machines Corporation (IBM) into the largest manufacturer of electric typewriters and data-processing equipment in the world.
    </p>
    <ul>
        <li>In 1939, he received an honorary degree in Doctor of Commercial Science from Oglethorpe University. </li>
        <li>In 1940s, Watson was on the national executive board of the Boy Scouts of America. </li>
        <li>Watson served as a trustee of Columbia University from June 6, 1933, until his death. </li>
        <li>He was posthumously inducted into the Junior Achievement U.S. Business Hall of Fame in 1990.</li>
    </ul>
</body>
</html>
```

Go to the **File** menu and click **Save** to save your code.<br>

The resulting page looks like this.

![List](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-CD0101EN-SkillsNetwork/labs/Theia%20Labs/01%20-%20HTML%20and%20CSS/Lab%201%20HTML/images/7.png)

::page{title="Add a Table"}

A table is created using the `<table>` tag.<br>

Within the table, each row of data is represented using the `<tr>` (table row) tag.<br>

The column or row headings can be specified by the `<th>` (table heading) element.<br>

Finally, each data element within the table cells is specified using the `<td>` (table data) tag.<br>

Let\'s add a heading and a table with three rows and two columns.<br>

Type the below code after the `</ul>` tag.<br>

```html
<h1>IBM Growth Over Years: </h1>
<table>
    <tr>
        <th>Year </th>
        <th>No. of Employees </th>
        <th>Gross Income (In m$) </th>
    </tr>
    <tr>
        <td>1925</td>
        <td>3698</td>
        <td>13</td>
    </tr>
    <tr>
        <td>1930</td>
        <td>6346</td>
        <td>19 </td>
    </tr>
    <tr>
        <td>1935</td>
        <td>8651</td>
        <td>21</td>
    </tr>
    
</table>
```

Your code should look like this now.<br>

```html
<!DOCTYPE html>
<html>
<head>
    <title>Thomas J. Watson Sr -  Fan Page</title>
</head>
<body>
    <h1>Thomas J. Watson </h1>
    <img src="https://upload.wikimedia.org/wikipedia/commons/7/7e/Thomas_J_Watson_Sr.jpg" width="300" height="300">

    <p>Thomas J. Watson, Sr. is the American industrialist, who built the International Business Machines Corporation (IBM) into the largest manufacturer of electric typewriters and data-processing equipment in the world.
    </p>
    <ul>
        <li>In 1939, he received an honorary degree in Doctor of Commercial Science from Oglethorpe University. </li>
        <li>In 1940s, Watson was on the national executive board of the Boy Scouts of America. </li>
        <li>Watson served as a trustee of Columbia University from June 6, 1933, until his death. </li>
        <li>He was posthumously inducted into the Junior Achievement U.S. Business Hall of Fame in 1990.</li>
    </ul>
    
    <h1>IBM Growth Over Years: </h1>
    <table>
        <tr>
            <th>Year </th>
            <th>No. of Employees </th>
            <th>Gross Income (In m$) </th>
        </tr>
        <tr>
            <td>1925</td>
            <td>3698</td>
            <td>13</td>
        </tr>
        <tr>
            <td>1930</td>
            <td>6346</td>
            <td>19 </td>
        </tr>
        <tr>
            <td>1935</td>
            <td>8651</td>
            <td>21</td>
        </tr>
        
    </table>
        
</body>
</html>
```

Go to the **File** menu and click **Save** to save your code.<br>

The resulting table looks like this.

![Table](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-CD0101EN-SkillsNetwork/labs/Theia%20Labs/01%20-%20HTML%20and%20CSS/Lab%201%20HTML/images/8.png)

 

::page{title="Add Links to other pages"}

Web pages connect to other web pages and files using hyperlinks.<br> 

A hyperlink is created using the anchor tag `<a>`.<br>

Once you click the link, the `href` attribute tells the browser which web page you should be taken to.<br>

Let\'s create a link to the official web page of IBM from the current page.<br>

Within the main paragraph there is a reference to **IBM**, where we\'ll add the link.<br>

Find the word IBM in the first paragraph and replace it with the code below.<br>

```html
 <a href="https://www.ibm.com">IBM</a>
```

Here is the complete HTML code of the web page.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Thomas J. Watson Sr -  Fan Page</title>
</head>
<body>
    <h1>Thomas J. Watson </h1>
    <img src="https://upload.wikimedia.org/wikipedia/commons/7/7e/Thomas_J_Watson_Sr.jpg" width="300" height="300">

    <p>Thomas J. Watson, Sr. is the American industrialist, who built the International Business Machines Corporation (<a href="https://www.ibm.com">IBM</a>)  into the largest manufacturer of electric typewriters and data-processing equipment in the world.
    </p>
    <ul>
        <li>In 1939, he received an honorary degree in Doctor of Commercial Science from Oglethorpe University. </li>
        <li>In 1940s, Watson was on the national executive board of the Boy Scouts of America. </li>
        <li>Watson served as a trustee of Columbia University from June 6, 1933, until his death. </li>
        <li>He was posthumously inducted into the Junior Achievement U.S. Business Hall of Fame in 1990.</li>
    </ul>
    
    <h1>IBM Growth Over Years: </h1>
    <table>
        <tr>
            <th>Year </th>
            <th>Employees </th>
            <th>Gross Income (In m$) </th>
        </tr>
        <tr>
            <td>1925</td>
            <td>3698</td>
            <td>13</td>
        </tr>
        <tr>
            <td>1930</td>
            <td>6346</td>
            <td>19 </td>
        </tr>
        <tr>
            <td>1935</td>
            <td>8651</td>
            <td>21</td>
        </tr>
        
    </table>
        
</body>
</html>
```

Go to the **File** menu and click **Save** to save your code.<br>

You should then see the hyperlink like this.<br>

![Hyperlink](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-CD0101EN-SkillsNetwork/labs/Theia%20Labs/01%20-%20HTML%20and%20CSS/Lab%201%20HTML/images/hyperlink.png)

When you click the hyperlink, your browser will navigate to the IBM website.
    

::page{title="Add a Feedback Form"}

    
Let\'s create a feedback form to collect user input. Forms are an essential part of web development, allowing for the collection and submission of data to a server. They provide an interactive way for users to enter text, make selections, and submit information for processing. 
To build this form, we will use the following HTML elements:  

- **`<form>`**:  
  Defines the structure of the form and acts as a container for all form-related elements. It specifies where and how the collected data should be submitted.  

- **`<input>`**:  
  Collects user input through various types such as text, email, password, and more, allowing for single-line data entry.  

- **`<textarea>`**:  
  Allows users to input larger amounts of text, such as comments or feedback, providing a scrollable, multi-line input area.  

- **`<button>`**:  
  Used to trigger specific actions, such as submitting or resetting the form. The behavior is determined by the `type` attribute.  

- **`<label>`**:  
  Provides a textual description or context for form controls, improving usability and accessibility, especially for screen readers.  

- **`<fieldset>`**:  
  Groups related elements in a form, visually and logically organizing them. Often used with a `<legend>` to describe the group.  
    
Add the following code after the table:
    
```html
    <h2>Insights Submission Form</h2>
    <form action="/submit-feedback" method="POST">
        <fieldset>
            <legend>Your Insights About Thomas J. Watson Are Valued</legend>
    
            <!-- Name Field -->
            <label for="name">Name:</label><br>
            <input type="text" id="name" name="name" placeholder="Enter your name" required><br><br>
    
            <!-- Email Field -->
            <label for="email">Email:</label><br>
            <input type="email" id="email" name="email" placeholder="Enter your email" required><br><br>
    
            <!-- Comments Field -->
            <label for="comments">Comments:</label><br>
            <textarea id="comments" name="comments" rows="4" cols="50" placeholder="Share your thoughts about Thomas J. Watson"></textarea><br><br>
    
            <!-- Submit Button -->
            <button type="submit">Submit</button>
        </fieldset>
    </form>
```

The resulting feedback form is shown below. For your reference, we have labeled the form elements in the accompanying screenshot.

![form1.png](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/08VQMhAu8CII5-Hkq8abjQ/form1.png)
### Updated Full HTML Code
    
Here\'s the complete updated HTML code, including the feedback form:
    
```html
<!DOCTYPE html>
<html>
<head>
    <title>Thomas J. Watson Sr -  Fan Page</title>
</head>
<body>
    <h1>Thomas J. Watson </h1>
    <img src="https://upload.wikimedia.org/wikipedia/commons/7/7e/Thomas_J_Watson_Sr.jpg" width="300" height="300">

    <p>Thomas J. Watson, Sr. is the American industrialist, who built the International Business Machines Corporation (<a href="https://www.ibm.com">IBM</a>)  into the largest manufacturer of electric typewriters and data-processing equipment in the world.
    </p>
    <ul>
        <li>In 1939, he received an honorary degree in Doctor of Commercial Science from Oglethorpe University. </li>
        <li>In 1940s, Watson was on the national executive board of the Boy Scouts of America. </li>
        <li>Watson served as a trustee of Columbia University from June 6, 1933, until his death. </li>
        <li>He was posthumously inducted into the Junior Achievement U.S. Business Hall of Fame in 1990.</li>
    </ul>
    
    <h1>IBM Growth Over Years: </h1>
    <table>
        <tr>
            <th>Year </th>
            <th>Employees </th>
            <th>Gross Income (In m$) </th>
        </tr>
        <tr>
            <td>1925</td>
            <td>3698</td>
            <td>13</td>
        </tr>
        <tr>
            <td>1930</td>
            <td>6346</td>
            <td>19 </td>
        </tr>
        <tr>
            <td>1935</td>
            <td>8651</td>
            <td>21</td>
        </tr>
        
    </table>

    <h2>Insights Submission Form</h2>
    <form action="/submit-feedback" method="POST">
        <fieldset>
            <legend>Your Insights About Thomas J. Watson Are Valued</legend>
    
            <!-- Name Field -->
            <label for="name">Name:</label><br>
            <input type="text" id="name" name="name" placeholder="Enter your name" required><br><br>
    
            <!-- Email Field -->
            <label for="email">Email:</label><br>
            <input type="email" id="email" name="email" placeholder="Enter your email" required><br><br>
    
            <!-- Comments Field -->
            <label for="comments">Comments:</label><br>
            <textarea id="comments" name="comments" rows="4" cols="50" placeholder="Share your thoughts about Thomas J. Watson"></textarea><br><br>
    
            <!-- Submit Button -->
            <button type="submit">Submit</button>
        </fieldset>
    </form>
</body>

</html>
```

You should now see the complete web page using the Live Server extension. It should resemble the following page:<br>


![full_output.png](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/nQkJA651om7D0yI0O7-EPQ/full-output.png)

::page{title="Congratulations"}

Congratulations!!! You have created your first web page.<br>
If you haven\'t already done so, you should try creating a web page with your own details.<br> 

### Author(s)

<h5> Ramesh Sannareddy <h5/>

#### Other Contributor(s) 

<h5> Michelle Saltoun <h5/>
	
<h3 align="center"> &#169; IBM Corporation. All rights reserved. <h3/>
<!--
## Changelog

| Date | Version | Changed by | Change Description |
|------|--------|--------|---------|
| 2024-12-30 |--------|Prashant Juyal|QA edits|
| 2020-08-13 | 1.0 | Ramesh Sannareddy | Initial version created |
| 2022-09-13 | 1.1 | Michelle Saltoun | Minor Updates |
| 2024-11-20 | 1.2 | Manvi Gupta | Updated estimated time and remove extra spaces |
| 2024-11-21 | 1.3 | Rajashree Patil | Enhancement: Added Feedback form |
| 2025-11-21 | 1.4| Vandana Pandey | Changed form screenshot and create file screenshot|
## <h3 align="center"> Â© IBM Corporation. All rights reserved. <h3/>-->
