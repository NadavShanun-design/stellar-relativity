/* stellar-relativity web viz — all relativity math done client-side so the
 * speed slider recomputes live. Mirrors the Python package formulas. */
(function () {
  "use strict";

  var stars = (window.STAR_DATA && window.STAR_DATA.stars) || [];
  var canvas = document.getElementById("sky");
  var ctx = canvas.getContext("2d");
  var slider = document.getElementById("speed");
  var speedLabel = document.getElementById("speedLabel");
  var tbody = document.querySelector("#starTable tbody");

  var MAX_LY = 26; // ring radius reference

  function lorentz(beta) { return 1 / Math.sqrt(1 - beta * beta); }

  function travel(distanceLy, beta) {
    var earth = distanceLy / beta;
    var proper = earth / lorentz(beta);
    return { earth: earth, proper: proper, saved: earth - proper };
  }

  // Project equatorial (ra hours, dec deg) onto a top-down x/y map (z -> depth).
  function project(star) {
    var ra = (star.ra_hours * 15) * Math.PI / 180;
    var dec = star.dec_deg * Math.PI / 180;
    var x = star.distance_ly * Math.cos(dec) * Math.cos(ra);
    var y = star.distance_ly * Math.cos(dec) * Math.sin(ra);
    var z = star.distance_ly * Math.sin(dec);
    return { x: x, y: y, z: z };
  }

  function draw(beta) {
    var w = canvas.width, h = canvas.height;
    var cx = w / 2, cy = h / 2;
    var scale = (Math.min(w, h) / 2 - 24) / MAX_LY;
    ctx.clearRect(0, 0, w, h);

    // reference rings
    ctx.strokeStyle = "#1d2142";
    [5, 10, 25].forEach(function (r) {
      ctx.beginPath();
      ctx.arc(cx, cy, r * scale, 0, Math.PI * 2);
      ctx.stroke();
      ctx.fillStyle = "#4a5080";
      ctx.font = "10px sans-serif";
      ctx.fillText(r + " ly", cx + 3, cy - r * scale + 12);
    });

    // the Sun
    ctx.fillStyle = "#ffd166";
    ctx.beginPath();
    ctx.arc(cx, cy, 5, 0, Math.PI * 2);
    ctx.fill();
    ctx.fillStyle = "#8b93c0";
    ctx.fillText("Sun", cx + 8, cy + 4);

    stars.forEach(function (star) {
      var p = project(star);
      var px = cx + p.x * scale;
      var py = cy - p.y * scale;
      // depth (z) -> brightness; closer-to-us-in-z is brighter
      var depth = Math.max(0, 1 - Math.abs(p.z) / MAX_LY);
      var size = 2 + 4 * (1 - star.distance_ly / MAX_LY);
      ctx.fillStyle = "rgba(170,195,255," + (0.35 + 0.55 * depth).toFixed(3) + ")";
      ctx.beginPath();
      ctx.arc(px, py, Math.max(1.5, size), 0, Math.PI * 2);
      ctx.fill();
    });
  }

  function renderTable(beta) {
    var rows = stars.slice().sort(function (a, b) { return a.distance_ly - b.distance_ly; });
    tbody.innerHTML = rows.map(function (s) {
      var t = travel(s.distance_ly, beta);
      return "<tr><td>" + s.name + "</td><td>" + s.distance_ly.toFixed(2) +
        "</td><td>" + t.earth.toFixed(2) + "</td><td>" + t.proper.toFixed(2) +
        "</td><td>" + t.saved.toFixed(2) + "</td></tr>";
    }).join("");
  }

  function update() {
    var beta = Number(slider.value) / 100;
    speedLabel.textContent = slider.value + "%";
    draw(beta);
    renderTable(beta);
  }

  if (!stars.length) {
    tbody.innerHTML = "<tr><td colspan='5'>No data loaded (data.js missing).</td></tr>";
    return;
  }
  slider.addEventListener("input", update);
  update();
})();
