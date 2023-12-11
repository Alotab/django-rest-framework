import "https://flackr.github.io/scroll-timeline//dist/scroll-timeline.js";

/*====================== GLOBAL VARIABLES ========================*/
var windowWidth = window.innerWidth;
var ipadMaxWidth = 768;
let mobileMaxWidth = 480;



/*============ SHOW MENU =================== */
const primaryNav = document.querySelector('.primary-navigation');
const navToggleMobile = document.querySelector('.mobile-nav-toggle');
const navCloseToggle = document.querySelector('.mobile-nav-toggle-close');

const elSearcIcon = document.querySelector('.search-icon');
const elSearchMenu = document.querySelector('.middle-colume-search');


/*============== middle search bar =====================*/
if(elSearcIcon){
    elSearcIcon.addEventListener('click', ()=>{
        elSearchMenu.classList.add('middle-search');
    })
}


/*============== scroll tracker =====================*/
const scrollTracker = document.querySelector('.scroll-tracker');

const scrollTrackingTimeline = new ScrollTimeline({
    // by default source is the entire viewpower for the scorlling elmenet
    source: document.scrollingElement, 
    //for up/down (block) scrolling and horizontall scorlling
    orientation: "block", 
    //scrolling range /starting point and end point
    scrollOffsets: [CSS.percent(0), CSS.percent(120)]
});

scrollTracker.animate(
    {
        transform: ["scaleX(0", "scale(1"],
    },
    {
        duration: 1,
        timeline: scrollTrackingTimeline,
    }
);


/*=============== Hambuger Menu for small devices =================*/

// prevent and enable scrolling when hambuger menu is clicked
function disableScroll() {
    // Get the current page scroll position
    // var scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    // var scrollLeft = window.pageXOffset || document.documentElement.scrollLeft;
     var scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
    var scrollLeft = document.documentElement.scrollLeft || document.body.scrollLeft;
  
        // if any scroll is attempted, set this to the previous value
        window.onscroll = function() {
            window.scrollTo(scrollLeft, scrollTop);
        };
}
function enableScroll() {
    window.onscroll = function() {};
}  

navToggleMobile.addEventListener('click', () => {
    const visibility = primaryNav.getAttribute('data-visible');
    // const hamMenuVisibility = navToggleMobile.getAttribute('data-visible');
    // const closeMenuVisiblity =  navCloseToggle.getAttribute('data-visible');
   
    // Get the window object.
    var window = window;

    disableScroll();
    if(visibility === "false"){
        primaryNav.setAttribute('data-visible', true);
        navToggleMobile.setAttribute('aria-expanded', true);
        navCloseToggle.setAttribute('aria-expanded', true);
    } 
});
navCloseToggle.addEventListener('click', () => {
    const visibility = primaryNav.getAttribute('data-visible');

    enableScroll();
    if(visibility === 'true'){
        navCloseToggle.setAttribute('aria-expanded', false);
        primaryNav.setAttribute('data-visible', false);  
        navToggleMobile.setAttribute('aria-expanded', false);
    }
});
function preventScrolling() {
    document.addEventListener('click', function(event) {
        if (event.target.classList.contains('mobile-nav-toggle')) {
        event.preventDefault();
        document.body.classList.add('no-scroll');
        } else if (event.target.classList.contains('close-menu')) {
        document.body.classList.remove('no-scroll');
        }
    });
}
window.onload = preventScrolling;


/*=============== EXTERNAL LINK SCREEN  ===============*/
const detailImage = document.querySelector(".post-image");
const postdetailOne = document.querySelector(".post-main-detail");

const externalOne = document.querySelector(".external-share-container");
const sharelinkOne = document.querySelector(".share-link");
const shareScroll = document.querySelector(".share-scroll");
const foot = document.querySelector('footer');
const footer = document.querySelector(".main-detail-post");


    
function addShareScrollBig(){
    const scrollPosition = window.scrollY;
    
// scrollPosition >= 130
    //// Triggers when the Bottom toolbar is visible on mobile
    if(foot){
        // if(windowWidth <= mobileMaxWidth && scrollPosition >= 130){
        //     shareScroll.classList.add('active');
        //     // shareScroll.style.backgroundColor = "red";
        //     shareScroll.classList.remove('share-scroll-position');
        // }
        if(windowWidth <= mobileMaxWidth && scrollPosition <= foot.offsetTop - 650){
            shareScroll.classList.add('active');
            shareScroll.classList.remove('share-scroll-position');
        }
        if(windowWidth <= mobileMaxWidth && scrollPosition >= foot.offsetTop - 650 || scrollPosition <= 130){
            shareScroll.classList.remove('active');
            shareScroll.classList.add('share-scroll-position');
        } 
    }
   
   
    /// Triggers on Desktop
    // const shareBoxOffset = externalOne.offsetTop;
    // scrollPosition <= foot.offsetTop - 700
    // scrollPosition <= shareBoxOffset - 700
    if(externalOne){
        const shareBoxOffset = externalOne.offsetTop;
        if(scrollPosition <= shareBoxOffset - 700){
            shareScroll.classList.add('active');
            shareScroll.classList.remove('share-scroll-position');
        }
        
        if(scrollPosition >= shareBoxOffset - 700 || scrollPosition <= 130){
            shareScroll.classList.remove('active');
            shareScroll.classList.add('share-scroll-position');
        }
    }
    
  
  

    /// Triggers when Mobile Bottom Toolbar is Invincible. Use if possible for mobile defualt: cry:>
    if(externalOne){
        if(windowWidth <= ipadMaxWidth && scrollPosition >= externalOne.offsetTop){
            shareScroll.classList.remove('share-scroll-position');
        }
        if(windowWidth <= ipadMaxWidth && scrollPosition <= externalOne.offsetTop - 630){
            shareScroll.classList.add('active');
            shareScroll.classList.remove('share-scroll-position');
        }
        
        if(windowWidth <= ipadMaxWidth && scrollPosition >= externalOne.offsetTop - 630 || scrollPosition <= 130){
            shareScroll.classList.remove('active');
            shareScroll.classList.add('share-scroll-position');
        }
    }
 
}

window.addEventListener("scroll", addShareScrollBig);






/*=============== POPUP SHARE LIKE SCREEN ===============*/
const shareEl = document.querySelector('.share-share');
const removeMouse = document.querySelectorAll('.social-share i');
const socialContainerEl = document.querySelector('.social-scroll-wrapper');
const hidePopupWidget = document.querySelector('.kat');


let showMes = false;
// var showWidget = true;

function popShareScreen(){
    if(shareEl){
        shareEl.addEventListener('click', () => {
            socialContainerEl.classList.add('show-social-links');
            likePop.classList.remove('alert-active');
            removeMouse.forEach((icon) => {
                icon.style.cursor = 'default';
            });
            
            showMes = true;
            if(showMes){
                document.body.style.overflow = 'hidden';
            }
        
            document.addEventListener('mousedown', (e) => {
                if (!socialContainerEl.contains(e.target) && !shareEl.contains(e.target)) {
                    socialContainerEl.classList.remove('show-social-links');
                    document.body.style.overflow = 'auto';

                    removeMouse.forEach((icon) => {
                        icon.style.setProperty('cursor', "pointer", "important");
                    });
                  
                }
            });    
        });
    }
};
popShareScreen();






const likeMouseOver = document.querySelector('.share-like');
const commentMouseOver = document.querySelector('.share-comment');
const bookmarkMouseOver = document.querySelector('.share-bookmark');
const shareMouseOver = document.querySelector('.share-share');
const likePop = document.querySelector('.pop-like');
const commentPop = document.querySelector('.pop-comment');
const bookmarkPop = document.querySelector('.pop-bookmark');
const sharePop = document.querySelector('.pop-share');


// show widget on Large Screen or Desktop where mouseOver works
function desktopWidget() {
    if(likeMouseOver) {
        likeMouseOver.addEventListener('mouseover', () =>{

            setTimeout(() => {
                likePop.classList.add('alert-active');
            }, 10);
            likeMouseOver.addEventListener('mouseout', () =>{
                likePop.classList.remove('alert-active');
            })
        });
    }

    if(commentMouseOver){
        commentMouseOver.addEventListener('mouseover', () =>{
            setTimeout(() => {
                commentPop.classList.add('alert-active');
            }, 10);
            commentMouseOver.addEventListener('mouseout', () =>{
                commentPop.classList.remove('alert-active');
            })
        });
    }
    if(bookmarkMouseOver){
        bookmarkMouseOver.addEventListener('mouseover', () =>{
            setTimeout(() => {
                bookmarkPop.classList.add('alert-active');
            }, 10);
            bookmarkMouseOver.addEventListener('mouseout', () =>{
                bookmarkPop.classList.remove('alert-active');
            })
        });
    }
    if(shareMouseOver){
        shareMouseOver.addEventListener('mouseover', () =>{
            setTimeout(() => {
                sharePop.classList.add('alert-active');
            }, 10);
            shareMouseOver.addEventListener('mouseout', () =>{
                sharePop.classList.remove('alert-active');
            })
        });
    }
};

if(windowWidth >= ipadMaxWidth + 10){
    desktopWidget();
}

// show widget on mobile or Tablet where mouseOver works
// var ipadMaxWidth = 768;
// let mobileMaxWidth = 480;

const removeHover = document.querySelector('.social-share i');

function mobileTabletWidget() {
    if(likeMouseOver){
        likeMouseOver.addEventListener('touchstart', (e) =>{
            $(removeHover).removeClass('hover');
            likePop.classList.add('alert-active');
            
            setTimeout(() => {
                likePop.classList.remove('alert-active');
            }, 900);
        })
    }
    if(commentMouseOver){
        commentMouseOver.addEventListener('touchstart', () =>{
             $(removeHover).removeClass('hover');
            commentPop.classList.add('alert-active');
            setTimeout(() => {
                commentPop.classList.remove('alert-active');
            }, 900);
        });
    }
    if(bookmarkMouseOver){
        bookmarkMouseOver.addEventListener('touchstart', () =>{
            bookmarkPop.classList.add('alert-active');
            setTimeout(() => {
                bookmarkPop.classList.remove('alert-active');
            }, 900);
        });
    }
    if(shareMouseOver){
        shareMouseOver.addEventListener('touchstart', () =>{
            sharePop.classList.add('alert-active');
            setTimeout(() => {
                sharePop.classList.remove('alert-active');
            }, 900);
        });
    }
    
}

if(windowWidth <= mobileMaxWidth){
    mobileTabletWidget();
}




/*=============== SCROLL REVEAL ANIMATION ===============*/
const sr = ScrollReveal({
    origin: 'top',
    distance: '60px',
    duration: 2500,
    delay: 400
});
sr.reveal(`.home__data, .footer__container, .footer__group`);
sr.reveal(`.portfolio-container, .portfolio-card`, {delay: 700, origin: 'bottom'});
sr.reveal(`.portfolio-container, .portfolio-card`, {interval: 100});
sr.reveal(`.my-profile-introduction`, {origin: 'left'});
sr.reveal(`.my-profile-image`, {origin: 'right'});



/*================= REDIRECT TO EXTERNAL SOCIAL APP ===================*/
// Get all share buttons
const shareButtons = document.querySelectorAll('.share-button');

// Add click event listener to each button
shareButtons.forEach(button => {
   button.addEventListener('click', (e) => {
      e.preventDefault();

      // Get the URL of the current page
      const url = window.location.href;

      // Get the social media platform from the button's class name
      const platform = button.classList[1];

      // Set the URL to share based on the social media platform
      let shareUrl;
      switch (platform) {
         case 'facebook':
         shareUrl = `https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(url)}`;
         break;
         case 'twitter':
         shareUrl = `https://twitter.com/share?url=${encodeURIComponent(url)}`;
         break;
         case 'linkedin':
         shareUrl = `https://www.linkedin.com/shareArticle?url=${encodeURIComponent(url)}`;
         break;
         case 'reddit':
         shareUrl = `https://reddit.com/submit?url=${encodeURIComponent(url)}`;
         break;
         case 'whatsapp':
         shareUrl = `https://api.whatsapp.com/send?text=${encodeURIComponent(url)}`;
         break;
      }

      // Open a new window to share the URL
      window.open(shareUrl, '_blank');
   });
});

// copy permalink/url when user click permalink button
const button = document.querySelector('.permalink');
const copyArticl = document.querySelector('.permalink-message');

function permalinkShare(){
    if(button){
        button.addEventListener('click', (e) => {

            e.preventDefault()
            const url = window.location.href;
            const copied = navigator.clipboard.writeText(url);
        
            if (copied) {
                copyArticl.classList.add('show-permalink-message');
                e.preventDefault();
        
                setTimeout(()=>{
                    copyArticl.classList.remove('show-permalink-message');
                }, 1500);
            } 
        });
    };
}
permalinkShare();

/*========================= DARK MODE =======================   activate-mode */
const setDarkEl = document.querySelector('.darkmode-setup');
const setSunsetEl = document.querySelector('.sunset-setup');
// const darkModeToggler = document.querySelector('.darkmode-set');

setDarkEl.addEventListener('click', () => {
    if(setDarkEl){
        setDarkEl.setAttribute('aria-expanded', true);
        setSunsetEl.setAttribute('aria-expanded', true);
        document.body.classList.toggle("dark-mode-theme");


        //update the local storage when user click on the button
        if(localStorage.getItem("theme") == "light"){
            localStorage.setItem("theme", "dark");
        } else{
            localStorage.setItem("theme", "light");
        }
    }
});

setSunsetEl.addEventListener('click', () => {
    if(setSunsetEl){
        setSunsetEl.setAttribute('aria-expanded', false);
        setDarkEl.setAttribute('aria-expanded', false);
        document.body.classList.remove("dark-mode-theme");

        //update the local storage when user click on the button
        if(localStorage.getItem("theme") == "dark"){
            localStorage.setItem("theme", "light");
        } else {
            localStorage.setItem("theme", "light");
        }
    }
});


if(localStorage.getItem("theme") == "light"){
    document.body.classList.remove("dark-mode-theme");
} else if(localStorage.getItem("theme") == "dark"){
    document.body.classList.add("dark-mode-theme");
} else {
    // execute when a user first the website for the first time
    localStorage.setItem("theme", "light");
};
