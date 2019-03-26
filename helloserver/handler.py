def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """

    html = """
<!DOCTYPE html>
<html>
<body>

<!-- This is a comment -->
<p>This is a great webpage.</p>
<!-- Comments are not displayed in the browser -->

</body>
</html>
    """
    return html
