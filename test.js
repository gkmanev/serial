const http = require('http');
const url = 'http://localhost:1880/admin/updateFlow';
const payload = JSON.stringify({
  flowId: 'myFlowId',
  id: 'myNodeId',
  disabled: false
});

http.post(url, {
  headers: {
    'Content-Type': 'application/json'
  },
  body: payload
}).then(() => {
  console.log('Node enabled');
}).catch(error => {
  console.error('Error enabling node:', error);
});
