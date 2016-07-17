$(function() {
    $('#vision').delay(2000).hide(500)
    window.setTimeout(function() {
        document.getElementById('vision').innerHTML = "The Vision"
    }, 2500)
    $('#vision').delay(2500).show(500)
})
