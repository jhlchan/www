---
title: Pyscript - Demo 3
header-includes: |
    <style>
       body { min-width: 90% !important; }
    </style>
include-before: |
    <script src="https://d3js.org/d3.v7.min.js"></script>
include-after: |
    <link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css"/>
    <script defer src="https://pyscript.net/latest/pyscript.js"></script>
    <!-- python -m http.server, URL: http://0.0.0.0:8000/demo/demo03.html -->
    <!-- file:///Users/josephchan/jc/www/python/pyscript/demo/demo03.html -->
---

# Pyscript - 2D Visualization by JavaScript

<!-- output target (nested divs) -->
::::::{#py width=400px height=400px}
:::{ .loading }
:::
::::::
<!--
<div id="py" style="width: 400px; height: 400px">
<div class="loading"></div>
</div>
-->

Type your Python code (hover mouse/pointer to bottom right-end for Green arrow to run code):
<py-repl></py-repl>

<!--
D3.js
The JavaScript library for bespoke data visualization
https://d3js.org 
Create custom dynamic visualizations with unparalleled flexibility
<script src="https://d3js.org/d3.v7.min.js"></script>

div = Element('py')
div.element.innerHTML

<svg viewBox="-320 -320 640 640" width="400" height="400"><path style="fill: steelblue;" d="M1,-301.866A8,8,0,0,1,9.238,- ... 1</tspan></text></svg>

An SVG image, no canvas.
-->

<!-- Javascript
<script type="module">
    const fruits = [
        { name: "🍊", count: 21 },
        { name: "🍇", count: 13 },
        { name: "🍏", count: 8 },
        { name: "🍌", count: 5 },
        { name: "🍐", count: 3 },
        { name: "🍋", count: 2 },
        { name: "🍎", count: 1 },
        { name: "🍉", count: 1 },
    ];

    const fn = (d) => d.count;
    const data = d3.pie().value(fn)(fruits);

    const arc = d3
        .arc()
        .innerRadius(210)
        .outerRadius(310)
        .padRadius(300)
        .padAngle(2 / 300)
        .cornerRadius(8);

    // element #js for Javscript, #py for Python, side-by-side
    const js = d3.select("#js");
    js.select(".loading").remove();

    const svg = js
        .append("svg")
        .attr("viewBox", "-320 -320 640 640")
        .attr("width", "400")
        .attr("height", "400");

    for (const d of data) {
        svg.append("path").style("fill", "steelblue").attr("d", arc(d));

        const text = svg
            .append("text")
            .style("fill", "white")
            .attr(
                "transform",
                `translate(${arc.centroid(d).join(",")})`,
            )
            .attr("text-anchor", "middle");

        text.append("tspan")
            .style("font-size", "24")
            .attr("x", "0")
            .text(d.data.name);

        text.append("tspan")
            .style("font-size", "18")
            .attr("x", "0")
            .attr("dy", "1.3em")
            .text(d.value);
    }
</script>
-->

<!-- pyscript -->
```{=html}
<py-script>
import js
from pyodide.ffi import create_proxy, to_js
from js import d3  # get D3 from d3.v7.min.js

# Python data
fruits = [
    {"name": "🍊", "count": 21},
    {"name": "🍇", "count": 13},
    {"name": "🍏", "count": 8},
    {"name": "🍌", "count": 5},
    {"name": "🍐", "count": 3},
    {"name": "🍋", "count": 2},
    {"name": "🍎", "count": 1},
    {"name": "🍉", "count": 1},
]

# Create JS function in Python
fn = create_proxy(lambda d, *_: d["count"])
# invoke JS function d3.pie().value(fn)
data = d3.pie().value(fn)(to_js(fruits))

# form a JS proxy
arc = (
    d3.arc()
    .innerRadius(210)
    .outerRadius(310)
    .padRadius(300)
    .padAngle(2 / 300)
    .cornerRadius(8)
)

# get the element
py = d3.select("#py")
py.select(".loading").remove()

# form a JS proxy
svg = (
    py.append("svg")
    .attr("viewBox", "-320 -320 640 640")
    .attr("width", "400")
    .attr("height", "400")
)

for d in data:
    # d is a JS object = Python dict
    d_py = d.to_py()

    # all done in JS proxy
    (svg.append("path").style("fill", "steelblue").attr("d", arc(d)))

    # all done in JS proxy
    text = (
        svg.append("text")
        .style("fill", "white")
        .attr("transform", f"translate({arc.centroid(d).join(',')})")
        .attr("text-anchor", "middle")
    )

    (
        text.append("tspan")
        .style("font-size", "24")
        .attr("x", "0")
        .text(d_py["data"]["name"])
    )

    (
        text.append("tspan")
        .style("font-size", "18")
        .attr("x", "0")
        .attr("dy", "1.3em")
        .text(d_py["value"])
    )
</py-script>
```
<!--
Browser console:
>> d3
Object { format: l(t), formatPrefix: formatPrefix(t, n), timeFormat: format(t), timeParse: parse(t), utcFormat: utcFormat(t), utcParse: utcParse(t), Adder: class T, Delaunay: class Lu, FormatSpecifier: tf(t), InternMap: class InternMap, … }
with a tree.
d3.pie             gives function pie()
d3.pie.toString()  gives the function

Python console:
d3.pie
function(){var ... }

Attributes of d3:

d3.__dir__()

['Adder', 'Delaunay', 'FormatSpecifier', 'InternMap', 'InternSet', 'Node', 'Path', 'Voronoi', 'ZoomTransform', '__bool__', '__class__', '__defineGetter__', '__defineSetter__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lookupGetter__', '__lookupSetter__', '__lt__', '__module__', '__ne__', '__new__', '__proto__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_js_type_flags', 'active', 'arc', 'area', 'areaRadial', 'as_object_map', 'ascending', 'autoType', 'axisBottom', 'axisLeft', 'axisRight', 'axisTop', 'bin', 'bisect', 'bisectCenter', 'bisectLeft', 'bisectRight', 'bisector', 'blob', 'blur', 'blur2', 'blurImage', 'brush', 'brushSelection', 'brushX', 'brushY', 'buffer', 'chord', 'chordDirected', 'chordTranspose', 'cluster', 'color', 'constructor', 'contourDensity', 'contours', 'count', 'create', 'creator', 'cross', 'csv', 'csvFormat', 'csvFormatBody', 'csvFormatRow', 'csvFormatRows', 'csvFormatValue', 'csvParse', 'csvParseRows', 'cubehelix', 'cumsum', 'curveBasis', 'curveBasisClosed', 'curveBasisOpen', 'curveBumpX', 'curveBumpY', 'curveBundle', 'curveCardinal', 'curveCardinalClosed', 'curveCardinalOpen', 'curveCatmullRom', 'curveCatmullRomClosed', 'curveCatmullRomOpen', 'curveLinear', 'curveLinearClosed', 'curveMonotoneX', 'curveMonotoneY', 'curveNatural', 'curveStep', 'curveStepAfter', 'curveStepBefore', 'descending', 'deviation', 'difference', 'disjoint', 'dispatch', 'drag', 'dragDisable', 'dragEnable', 'dsv', 'dsvFormat', 'easeBack', 'easeBackIn', 'easeBackInOut', 'easeBackOut', 'easeBounce', 'easeBounceIn', 'easeBounceInOut', 'easeBounceOut', 'easeCircle', 'easeCircleIn', 'easeCircleInOut', 'easeCircleOut', 'easeCubic', 'easeCubicIn', 'easeCubicInOut', 'easeCubicOut', 'easeElastic', 'easeElasticIn', 'easeElasticInOut', 'easeElasticOut', 'easeExp', 'easeExpIn', 'easeExpInOut', 'easeExpOut', 'easeLinear', 'easePoly', 'easePolyIn', 'easePolyInOut', 'easePolyOut', 'easeQuad', 'easeQuadIn', 'easeQuadInOut', 'easeQuadOut', 'easeSin', 'easeSinIn', 'easeSinInOut', 'easeSinOut', 'every', 'extent', 'fcumsum', 'filter', 'flatGroup', 'flatRollup', 'forceCenter', 'forceCollide', 'forceLink', 'forceManyBody', 'forceRadial', 'forceSimulation', 'forceX', 'forceY', 'format', 'formatDefaultLocale', 'formatLocale', 'formatPrefix', 'formatSpecifier', 'fsum', 'geoAlbers', 'geoAlbersUsa', 'geoArea', 'geoAzimuthalEqualArea', 'geoAzimuthalEqualAreaRaw', 'geoAzimuthalEquidistant', 'geoAzimuthalEquidistantRaw', 'geoBounds', 'geoCentroid', 'geoCircle', 'geoClipAntimeridian', 'geoClipCircle', 'geoClipExtent', 'geoClipRectangle', 'geoConicConformal', 'geoConicConformalRaw', 'geoConicEqualArea', 'geoConicEqualAreaRaw', 'geoConicEquidistant', 'geoConicEquidistantRaw', 'geoContains', 'geoDistance', 'geoEqualEarth', 'geoEqualEarthRaw', 'geoEquirectangular', 'geoEquirectangularRaw', 'geoGnomonic', 'geoGnomonicRaw', 'geoGraticule', 'geoGraticule10', 'geoIdentity', 'geoInterpolate', 'geoLength', 'geoMercator', 'geoMercatorRaw', 'geoNaturalEarth1', 'geoNaturalEarth1Raw', 'geoOrthographic', 'geoOrthographicRaw', 'geoPath', 'geoProjection', 'geoProjectionMutator', 'geoRotation', 'geoStereographic', 'geoStereographicRaw', 'geoStream', 'geoTransform', 'geoTransverseMercator', 'geoTransverseMercatorRaw', 'gray', 'greatest', 'greatestIndex', 'group', 'groupSort', 'groups', 'hasOwnProperty', 'hcl', 'hierarchy', 'histogram', 'hsl', 'html', 'image', 'index', 'indexes', 'interpolate', 'interpolateArray', 'interpolateBasis', 'interpolateBasisClosed', 'interpolateBlues', 'interpolateBrBG', 'interpolateBuGn', 'interpolateBuPu', 'interpolateCividis', 'interpolateCool', 'interpolateCubehelix', 'interpolateCubehelixDefault', 'interpolateCubehelixLong', 'interpolateDate', 'interpolateDiscrete', 'interpolateGnBu', 'interpolateGreens', 'interpolateGreys', 'interpolateHcl', 'interpolateHclLong', 'interpolateHsl', 'interpolateHslLong', 'interpolateHue', 'interpolateInferno', 'interpolateLab', 'interpolateMagma', 'interpolateNumber', 'interpolateNumberArray', 'interpolateObject', 'interpolateOrRd', 'interpolateOranges', 'interpolatePRGn', 'interpolatePiYG', 'interpolatePlasma', 'interpolatePuBu', 'interpolatePuBuGn', 'interpolatePuOr', 'interpolatePuRd', 'interpolatePurples', 'interpolateRainbow', 'interpolateRdBu', 'interpolateRdGy', 'interpolateRdPu', 'interpolateRdYlBu', 'interpolateRdYlGn', 'interpolateReds', 'interpolateRgb', 'interpolateRgbBasis', 'interpolateRgbBasisClosed', 'interpolateRound', 'interpolateSinebow', 'interpolateSpectral', 'interpolateString', 'interpolateTransformCss', 'interpolateTransformSvg', 'interpolateTurbo', 'interpolateViridis', 'interpolateWarm', 'interpolateYlGn', 'interpolateYlGnBu', 'interpolateYlOrBr', 'interpolateYlOrRd', 'interpolateZoom', 'interrupt', 'intersection', 'interval', 'isPrototypeOf', 'isoFormat', 'isoParse', 'js_id', 'json', 'lab', 'lch', 'least', 'leastIndex', 'line', 'lineRadial', 'link', 'linkHorizontal', 'linkRadial', 'linkVertical', 'local', 'map', 'matcher', 'max', 'maxIndex', 'mean', 'median', 'medianIndex', 'merge', 'min', 'minIndex', 'mode', 'namespace', 'namespaces', 'nice', 'now', 'object_entries', 'object_keys', 'object_values', 'pack', 'packEnclose', 'packSiblings', 'pairs', 'partition', 'path', 'pathRound', 'permute', 'pie', 'piecewise', 'pointRadial', 'pointer', 'pointers', 'polygonArea', 'polygonCentroid', 'polygonContains', 'polygonHull', 'polygonLength', 'precisionFixed', 'precisionPrefix', 'precisionRound', 'propertyIsEnumerable', 'quadtree', 'quantile', 'quantileIndex', 'quantileSorted', 'quantize', 'quickselect', 'radialArea', 'radialLine', 'randomBates', 'randomBernoulli', 'randomBeta', 'randomBinomial', 'randomCauchy', 'randomExponential', 'randomGamma', 'randomGeometric', 'randomInt', 'randomIrwinHall', 'randomLcg', 'randomLogNormal', 'randomLogistic', 'randomNormal', 'randomPareto', 'randomPoisson', 'randomUniform', 'randomWeibull', 'range', 'rank', 'reduce', 'reverse', 'rgb', 'ribbon', 'ribbonArrow', 'rollup', 'rollups', 'scaleBand', 'scaleDiverging', 'scaleDivergingLog', 'scaleDivergingPow', 'scaleDivergingSqrt', 'scaleDivergingSymlog', 'scaleIdentity', 'scaleImplicit', 'scaleLinear', 'scaleLog', 'scaleOrdinal', 'scalePoint', 'scalePow', 'scaleQuantile', 'scaleQuantize', 'scaleRadial', 'scaleSequential', 'scaleSequentialLog', 'scaleSequentialPow', 'scaleSequentialQuantile', 'scaleSequentialSqrt', 'scaleSequentialSymlog', 'scaleSqrt', 'scaleSymlog', 'scaleThreshold', 'scaleTime', 'scaleUtc', 'scan', 'schemeAccent', 'schemeBlues', 'schemeBrBG', 'schemeBuGn', 'schemeBuPu', 'schemeCategory10', 'schemeDark2', 'schemeGnBu', 'schemeGreens', 'schemeGreys', 'schemeOrRd', 'schemeOranges', 'schemePRGn', 'schemePaired', 'schemePastel1', 'schemePastel2', 'schemePiYG', 'schemePuBu', 'schemePuBuGn', 'schemePuOr', 'schemePuRd', 'schemePurples', 'schemeRdBu', 'schemeRdGy', 'schemeRdPu', 'schemeRdYlBu', 'schemeRdYlGn', 'schemeReds', 'schemeSet1', 'schemeSet2', 'schemeSet3', 'schemeSpectral', 'schemeTableau10', 'schemeYlGn', 'schemeYlGnBu', 'schemeYlOrBr', 'schemeYlOrRd', 'select', 'selectAll', 'selection', 'selector', 'selectorAll', 'shuffle', 'shuffler', 'some', 'sort', 'stack', 'stackOffsetDiverging', 'stackOffsetExpand', 'stackOffsetNone', 'stackOffsetSilhouette', 'stackOffsetWiggle', 'stackOrderAppearance', 'stackOrderAscending', 'stackOrderDescending', 'stackOrderInsideOut', 'stackOrderNone', 'stackOrderReverse', 'stratify', 'style', 'subset', 'sum', 'superset', 'svg', 'symbol', 'symbolAsterisk', 'symbolCircle', 'symbolCross', 'symbolDiamond', 'symbolDiamond2', 'symbolPlus', 'symbolSquare', 'symbolSquare2', 'symbolStar', 'symbolTimes', 'symbolTriangle', 'symbolTriangle2', 'symbolWye', 'symbolX', 'symbols', 'symbolsFill', 'symbolsStroke', 'text', 'thresholdFreedmanDiaconis', 'thresholdScott', 'thresholdSturges', 'tickFormat', 'tickIncrement', 'tickStep', 'ticks', 'timeDay', 'timeDays', 'timeFormat', 'timeFormatDefaultLocale', 'timeFormatLocale', 'timeFriday', 'timeFridays', 'timeHour', 'timeHours', 'timeInterval', 'timeMillisecond', 'timeMilliseconds', 'timeMinute', 'timeMinutes', 'timeMonday', 'timeMondays', 'timeMonth', 'timeMonths', 'timeParse', 'timeSaturday', 'timeSaturdays', 'timeSecond', 'timeSeconds', 'timeSunday', 'timeSundays', 'timeThursday', 'timeThursdays', 'timeTickInterval', 'timeTicks', 'timeTuesday', 'timeTuesdays', 'timeWednesday', 'timeWednesdays', 'timeWeek', 'timeWeeks', 'timeYear', 'timeYears', 'timeout', 'timer', 'timerFlush', 'toLocaleString', 'toString', 'to_py', 'transition', 'transpose', 'tree', 'treemap', 'treemapBinary', 'treemapDice', 'treemapResquarify', 'treemapSlice', 'treemapSliceDice', 'treemapSquarify', 'tsv', 'tsvFormat', 'tsvFormatBody', 'tsvFormatRow', 'tsvFormatRows', 'tsvFormatValue', 'tsvParse', 'tsvParseRows', 'typeof', 'union', 'unixDay', 'unixDays', 'utcDay', 'utcDays', 'utcFormat', 'utcFriday', 'utcFridays', 'utcHour', 'utcHours', 'utcMillisecond', 'utcMilliseconds', 'utcMinute', 'utcMinutes', 'utcMonday', 'utcMondays', 'utcMonth', 'utcMonths', 'utcParse', 'utcSaturday', 'utcSaturdays', 'utcSecond', 'utcSeconds', 'utcSunday', 'utcSundays', 'utcThursday', 'utcThursdays', 'utcTickInterval', 'utcTicks', 'utcTuesday', 'utcTuesdays', 'utcWednesday', 'utcWednesdays', 'utcWeek', 'utcWeeks', 'utcYear', 'utcYears', 'valueOf', 'variance', 'version', 'window', 'xml', 'zip', 'zoom', 'zoomIdentity', 'zoomTransform']


-->

---

<!-- pandoc -s demo03.md -o demo03.html -->