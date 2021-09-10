# How to intercept request/response with axios

```javascript
const axios = require("axios");

axios.interceptors.request.use((req) => {
  console.log(`${req.method} ${req.url}`);
  return req;
});

axios.interceptors.response.use((res) => {
  console.log(res.data);
  return res;
});
```
