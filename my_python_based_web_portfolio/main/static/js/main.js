document.addEventListener('DOMContentLoaded', function(){
  // reveal fade-up elements
  const els = document.querySelectorAll('.fade-up');
  const io = new IntersectionObserver((entries)=>{
    entries.forEach(entry=>{
      if(entry.isIntersecting){
        entry.target.classList.add('visible');
        io.unobserve(entry.target);
      }
    });
  }, {threshold:0.1});
  els.forEach(e=>io.observe(e));
});
