/* Lake Park Bicycles V2 - motion + UI */
(function(){
  function init(){
    // Sticky header: transparent at top -> tinted + blur past 40px
    var header = document.querySelector('header.site');
    if(header){
      var onScroll = function(){ header.classList.toggle('scrolled', window.scrollY > 40); };
      window.addEventListener('scroll', onScroll, {passive:true});
      onScroll();
    }

    // Mobile nav
    var menuBtn = document.getElementById('menuBtn');
    var nav = document.getElementById('mainnav');
    if(menuBtn && nav){
      menuBtn.addEventListener('click', function(){ nav.classList.toggle('open'); });
      nav.querySelectorAll('a').forEach(function(a){ a.addEventListener('click', function(){ nav.classList.remove('open'); }); });
    }

    // Scroll reveals (staggered), with a hard fallback so nothing stays hidden
    var items = Array.prototype.slice.call(document.querySelectorAll('[data-reveal]'));
    var show = function(el){ el.classList.add('in'); };
    if('IntersectionObserver' in window){
      var io = new IntersectionObserver(function(entries){
        entries.forEach(function(e){
          if(e.isIntersecting){
            var idx = items.indexOf(e.target);
            setTimeout(function(){ show(e.target); }, Math.min(idx,4)*60);
            io.unobserve(e.target);
          }
        });
      }, {threshold:0.12, rootMargin:'0px 0px -8% 0px'});
      items.forEach(function(el){ io.observe(el); });
    } else { items.forEach(show); }
    setTimeout(function(){ items.forEach(show); }, 2500);

    // Newsletter + contact toast (presentational for now)
    document.querySelectorAll('form[data-toast]').forEach(function(f){
      f.addEventListener('submit', function(e){ e.preventDefault(); f.reset(); toast(f.getAttribute('data-toast')); });
    });

    // Product detail: gallery / color / size selectors + add-to-cart
    var stage = document.getElementById('stageImg');
    document.querySelectorAll('.thumb').forEach(function(t){
      t.addEventListener('click', function(){
        if(stage) stage.src = t.getAttribute('data-full');
        document.querySelectorAll('.thumb').forEach(function(x){ x.classList.remove('active'); });
        t.classList.add('active');
      });
    });
    var colorLabel = document.getElementById('colorLabel');
    document.querySelectorAll('.swatch').forEach(function(s){
      s.addEventListener('click', function(){
        document.querySelectorAll('.swatch').forEach(function(x){ x.classList.remove('active'); });
        s.classList.add('active');
        if(colorLabel) colorLabel.textContent = s.getAttribute('data-color');
      });
    });
    document.querySelectorAll('.size').forEach(function(s){
      s.addEventListener('click', function(){
        document.querySelectorAll('.size').forEach(function(x){ x.classList.remove('active'); });
        s.classList.add('active');
      });
    });
    var addCart = document.getElementById('addCart');
    if(addCart) addCart.addEventListener('click', function(){ toast('Added to cart - see you at the shop'); });

    // Footer year
    var y = document.getElementById('yr'); if(y) y.textContent = new Date().getFullYear();
  }

  var toastEl;
  function toast(msg){
    if(!toastEl){
      toastEl = document.createElement('div');
      toastEl.style.cssText='position:fixed;left:50%;bottom:26px;transform:translate(-50%,140%);z-index:200;'+
        'background:#12a3a0;color:#fff;font-weight:600;letter-spacing:.01em;font-size:14px;'+
        'padding:15px 26px;border-radius:999px;box-shadow:0 16px 40px rgba(14,58,77,.35);transition:transform .4s cubic-bezier(.4,0,.2,1)';
      document.body.appendChild(toastEl);
    }
    toastEl.textContent = msg || 'Thanks - see you at the shop';
    requestAnimationFrame(function(){ toastEl.style.transform='translate(-50%,0)'; });
    clearTimeout(toastEl._t);
    toastEl._t = setTimeout(function(){ toastEl.style.transform='translate(-50%,140%)'; }, 2600);
  }

  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
