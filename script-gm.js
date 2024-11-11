// You need GM_xmlhttpRequest to use this
// with tampermonkey @grant GM_xmlhttpRequest

let glx = GM_xmlhttpRequest;
function ch() {
      return new Promise((resolve, reject) => {
          glx({
              method: "GET",
              url: "http://localhost:5000/get_hwid_status",
              onload: function(rp) {
                  if (rp.status === 200) {
                      const rs = JSON.parse(rp.responseText);
                      resolve(rs.status === "valid");
                  } else {
                      hx()
                      re()
                  }
              },
              onerror: function() {
                hx()
                re()
              }
          });
      });
  }

  function hx() {
      document.body.style.display = "none";  }

  function re() {
      window.location.href = "https://github.com/iAlperenS";
   }

  ch().then(isValid => {
      if (isValid) {
      } else {
          hx()
          re()
      }
  }).catch(error => {
      hx()
      re()
  });
