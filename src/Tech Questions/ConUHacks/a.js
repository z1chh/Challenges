(self.webpackChunk_N_E=self.webpackChunk_N_E||[])
.push([[917],{5626:function(e,t,n){(window.__NEXT_P=window.__NEXT_P||[])
    .push(["/challenges/0183",function(){return n(8291)}])}
    ,8291:function(e,t,n){"use strict";n.r(t);var s=n(7568),r=n(655),o=n(5893),a=n(7294),c=function(){var e,t=(0,a.useState)(0),n=t[0],c=t[1],i=(0,a.useState)(""),u=i[0],l=i[1],h=(0,a.useState)(""),d=h[0],f=h[1],x=(e=(0,s.Z)
    (function(e,t){var s;return(0,r.__generator)(this,function(r){switch(r.label){case 0:return[4,fetch("/api/auth",((s={}).method="POST",
    s.headers={"Content-Type":"application/json"},s.body=JSON.stringify({challenge:e,answer:t}),s)).then(function(e){return e.json()})
    .then(function(e){"yes"==e.response&&(4==n?f(e.finalKey):(l(e.nextMsg),c(e.nextMsgId)))})];case 1:return r.sent(),[2]}})}),
    function(t,n){return e.apply(this,arguments)}),$=function(e){e.preventDefault(),x("cb"+n,e.target.answer.value),e.target.reset()};
    return 0==n?(0,o.jsx)("div",{children:(0,o.jsxs)("form",{className:"mt-12 text-white text-center",onSubmit:$,children:
    [(0,o.jsx)("label",{children:"enter final key from challenge 1 to enter challenge 2: "}),(0,o.jsx)("br",{}),(0,o.jsx)("textarea",{className:"my-2 w-32 text-black",name:"answer"}),(0,o.jsx)("br",{}),(0,o.jsx)("button",{children:"submit"})]})}):
    (3==n&&console.log("indice: ce sont toutes des lettres minuscules"),(0,o.jsx)("div",{children:d?(0,o.jsxs)("p",{className:"text-white text-center m-16",children:
    ["Sweet! You found my friend. Hope he’s doing good. You proved yourself someone I can trust. Now we’re going to have to cooperate to bring down The Eversors. You passed the second set of challenges. You can now go to registration.conuhacks.io and submit the following key to the 2nd challenge: "
    ,(0,o.jsx)("b",{children:d}),(0,o.jsx)("br",{}),
    "You have 1 more set of challenges to conquer. To continue, visit /challenges/7867."]})
    :(0,o.jsxs)("div",{className:"text-white text-center m-16",children:
    [(0,o.jsx)("p",{children:u}),1==n?(0,o.jsx)("img",{src:"/assets/beex.png",className:"h-32 w-50% m-auto brightness-[1%]"}):
    (0,o.jsx)(o.Fragment,{}),2==n?(0,o.jsx)("a",{className:"mt-6 bold",href:"/assets/audiofile.txt",download:"audiofile.txt",children:"download"})
    :(0,o.jsx)(o.Fragment,{}),(0,o.jsxs)("form",{className:"mt-12",onSubmit:$,children:
    [(0,o.jsx)("textarea",{className:"w-32 text-black",name:"answer"}),(0,o.jsx)("br",{}),(0,o.jsx)("button",{children:"try your luck"})]})]})}))};
    t.default=c},7568:
    function(e,t,n){"use strict";function s(e,t,n,s,r,o,a){try{var c=e[o](a),i=c.value}catch(u){n(u);return}
    c.done?t(i):
    Promise.resolve(i).then(s,r)}function r(e){return function(){var t=this,n=arguments;return new Promise(function(r,o){var a=e.apply(t,n);
        function c(e){s(a,r,o,c,i,"next",e)}function i(e){s(a,r,o,c,i,"throw",e)}c(void 0)})}}n.d(t,{Z:function(){return r}})}}
    ,function(e){e.O(0,[774,888,179],function(){return e(e.s=5626)}),_N_E=e.O()}
]);