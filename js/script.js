(function(){
 const c=document.getElementById('stars'),x=c.getContext('2d'),cur=document.getElementById('cursor');
 let w=innerWidth,h=innerHeight,dpr=Math.min(devicePixelRatio||1,2),pts=[];
 function resize(){w=innerWidth;h=innerHeight;c.width=w*dpr;c.height=h*dpr;c.style.width=w+'px';c.style.height=h+'px';x.setTransform(dpr,0,0,dpr,0,0);pts=Array.from({length:Math.min(170,Math.floor(w*h/8500))},()=>({x:Math.random()*w,y:Math.random()*h,r:Math.random()*1.35+.15,a:Math.random()*.65+.15,s:Math.random()*.18+.03}));}
 function draw(){x.clearRect(0,0,w,h);for(const p of pts){p.y+=p.s;if(p.y>h)p.y=-2;x.globalAlpha=p.a*(.65+.35*Math.sin(Date.now()/900+p.x));x.fillStyle='#fff';x.beginPath();x.arc(p.x,p.y,p.r,0,Math.PI*2);x.fill();}requestAnimationFrame(draw);}
 addEventListener('resize',resize);resize();draw();
 addEventListener('pointermove',e=>{cur.style.left=e.clientX+'px';cur.style.top=e.clientY+'px';});
 const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting)e.target.classList.add('show')}),{threshold:.12});
 document.querySelectorAll('.reveal').forEach(el=>io.observe(el));
 document.querySelectorAll('.world,.node').forEach(card=>{
   card.addEventListener('mousemove',e=>{
     const r=card.getBoundingClientRect(),rx=((e.clientY-r.top)/r.height-.5)*-4,ry=((e.clientX-r.left)/r.width-.5)*4;
     if(innerWidth>900)card.style.transform=`perspective(900px) rotateX(${rx}deg) rotateY(${ry}deg) translateY(-6px)`;
   });
   card.addEventListener('mouseleave',()=>card.style.transform='');
 });
})();

(function(){
  const bar=document.getElementById('scrollProgress');
  const update=()=>{
    const h=document.documentElement.scrollHeight-innerHeight;
    bar.style.width=(h>0?(scrollY/h)*100:0)+'%';
  };
  addEventListener('scroll',update,{passive:true});
  update();

  const art=document.querySelector('.hero-art');
  if(art && innerWidth>900){
    addEventListener('pointermove',e=>{
      const x=(e.clientX/innerWidth-.5);
      const y=(e.clientY/innerHeight-.5);
      art.style.transform=`perspective(1200px) rotateY(${x*5}deg) rotateX(${y*-4}deg)`;
    });
    addEventListener('pointerleave',()=>art.style.transform='');
  }

  document.querySelectorAll('.stage-node').forEach((el,i)=>{
    el.style.transitionDelay=(i*45)+'ms';
  });
})();
