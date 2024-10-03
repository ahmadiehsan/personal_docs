# Passed by Value/Reference

## Overview

![](passed_by_value_reference/image2.jpg)

## Why Slices Will Passed by Reference

<img src="image1.jpg" style="width:4.00833in" />

Slices use an underlying array, so when Go tries to copy it, it'll copy the slice information instead of the underlying array.
