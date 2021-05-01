# [URL redirect/rewrite using the .htaccess file](https://my.bluehost.com/cgi/help/htaccess_redirect)

How do I redirect all links for www.example.com to example.com ?

**Create a 301 redirect forcing all http requests to use either www.example.com or example.com:**

  *  **Example 1 - Redirect example.com to www.example.com:**

```
    RewriteEngine On
    RewriteCond %{HTTP_HOST} !^www. example.com$ [NC]
    RewriteRule ^(.*)$ http://www.example.com/$1 [L,R=301]
```

  *  **Example 2 - Redirect www.example.com to example.com:**


```
    RewriteEngine on
    RewriteCond %{HTTP_HOST} ^www\. example\.com$
    RewriteRule ^/?$ "http\:\/\/example\.com\/" [R=301,L]
```
