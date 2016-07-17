$(function() {
    function changeText() {
        document.getElementById('vision').innerHTML = "The Vision"
    }

    $('#vision').delay(2000).hide(500)
    $('#vision').delay(2500).show(500)

    window.setTimeout(changeText, 2500)
})
