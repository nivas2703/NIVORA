# builder/header_html.py

def get_header_html(css_content):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NIVORA &mdash; Turning Ideas Into Intelligent Products</title>
    <meta name="description" content="NIVORA is the technology and innovation universe built by Nivas Bennabatthula &mdash; where ambitious ideas become intelligent products, meaningful experiences and new digital possibilities.">
    <meta name="keywords" content="NIVORA, Nivas Bennabatthula, CHECKRA, HOMORA, BUBORA, SAYORA, FOLIVIO, Technology Universe, AI Innovation, Software Engineering">
    <meta name="author" content="Nivas Bennabatthula">

    <!-- Open Graph / Meta -->
    <meta property="og:type" content="website">
    <meta property="og:title" content="NIVORA &mdash; Turning Ideas Into Intelligent Products">
    <meta property="og:description" content="A technology and innovation universe where ambitious ideas become intelligent products, meaningful experiences and new digital possibilities.">
    <meta property="og:image" content="assets/images/nivora-logo.png">

    <!-- Favicon -->
    <link rel="icon" type="image/png" href="assets/images/nivora-logo.png">

    <!-- Fonts: Inter & Plus Jakarta Sans -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">

    <style>
{css_content}
    </style>
</head>
<body>
    <!-- Subtle digital starfield & cursor glow -->
    <canvas id="starfield" class="starfield-canvas" aria-hidden="true"></canvas>
    <div id="cursor-glow" class="cursor-glow" aria-hidden="true"></div>
"""
