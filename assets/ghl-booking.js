/* Lake Park Bicycles - pipe website bookings into GoHighLevel.
   The wizard still submits to Netlify as always. This ALSO posts the same
   booking to a GHL inbound webhook so a GHL workflow can create the contact,
   drop it on the Bike Repair / Bike Rental calendar, and send the
   confirmation + reminder texts.

   TO ACTIVATE: paste the GHL inbound-webhook URL between the quotes below.
   Until then this is a no-op and the site behaves exactly as before. */
window.GHL_BOOKING_WEBHOOK = "";

window.sendToGHL = function (payload) {
  var url = window.GHL_BOOKING_WEBHOOK;
  if (!url) { return; }
  try {
    fetch(url, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
      keepalive: true
    }).catch(function () {});
  } catch (e) {}
};
