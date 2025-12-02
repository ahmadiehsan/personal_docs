# Passed by Value/Reference

## Overview

![](passed_by_value_reference/image2.jpg)

## Why Slices Will Passed by Reference

![](passed_by_value_reference/image1.jpg)

Slices use an underlying array, so when Go tries to copy it, it'll copy the slice information instead of the underlying array.
