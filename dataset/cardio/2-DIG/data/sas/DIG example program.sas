
libname dig v612 'C:\projects\data distribution\DIG Teaching set\';



proc format;
 value incr  0='No Event'
             1='First Event';

 value dth2r  0='Alive'
              1='Died';

 value trtr 0='Placebo'
            1='Digoxin';

 value sexr 1='Men'
            2='Women';

 value racer 1='White'
             2='Non-white';

 value methr 1='Radionuclide'
             2='Angiography'
		     3='2-D Echo';

 value chestr 1='<=0.55'
              2='>0.55';

 value functr 1='Class I'
              2='Class II'
		      3='Class III'
		      4='Class IV';

 value etiolr 1='Ischemic'
              2='Hypertensive'
		      4='Idiopathic'
		      7='Other';

 value dthr 1='Worsening Heart Failure'
            2='Other Cardiac'
		    3='Other Vascular'
		    4='Unknown'
		    5='Noncardiac, nonvascular';

 value yesno 0='No'
             1='Yes';

 value ejfr 1='0.25-0.45'
            2='<0.25';

 value causer 1='Ischemic'
              2='NonIsch.';

 value funct2r 1='NYHA I,II'
               2='NYHA III,IV';


data dig; set dig.dig;

/* REFORMATS FOR SUMMARY TABLES */
 if 0<chestx<=0.55 then ctratio=1; if chestx>0.55 then ctratio=2;
 if nsym>=4 then nsym=4;
 if chfetiol=1 then chfcause=1; if chfetiol=2 then chfcause=2;
   if chfetiol=4 then chfcause=4; if chfetiol=3 or chfetiol=5 or chfetiol=6 then chfcause=7;
 if diuretk=1 or diuret=1 then diuretic=1; if diuretk=0 and diuret=0 then      diuretic=0;

 if 0<ejf_per<25 then ejfgrp=2; if 25<=ejf_per<=45 then ejfgrp=1;
 if functcls in(1,2) then NYHAgrp=1; if functcls in(3,4) then nyhagrp=2;
 if chfetiol=1 then cause=1; if chfetiol>1 then cause=2;



* MEANS AND PROPORTIONS FOR NEJM TABLES 1-4 ;

proc tabulate data=dig noseps formchar=' __________' missing;
 class trtmt ;
 format trtmt trtr. ;
 var age ejf_per chfdur nhosp;
 tables age ejf_per chfdur nhosp,
      trtmt*((N *f=6.0) (mean *f=6.2) (median *f=6.1) (std *f=6.2))
            /condense rtspace=32 box='Means found in DIG Trial Tables 1 and 2';
run;


proc tabulate data=dig noseps formchar=' __________' missing;
 class trtmt sex race ejfmeth ctratio functcls nsym prevmi angina diabetes hyperten diguse chfcause diuretic aceinhib nitrates vasod digdose reason;
 format trtmt trtr. sex sexr. race racer. ejfmeth methr. ctratio chestr. functcls functr. prevmi yesno. angina yesno. diabetes yesno. hyperten yesno. diguse yesno. chfcause etiolr. diuretic yesno. aceinhib yesno. nitrates yesno. vasod yesno. reason dthr.;
 tables sex race ejfmeth ctratio functcls nsym prevmi angina 
   diabetes hyperten diguse chfcause diuretic aceinhib nitrates vasod digdose reason,
      trtmt*((N *f=8.0) (colpctn *f=8.1))
            /condense rtspace=42 box='Proportions: DIG Trial Tables 1 and 2';
run;










proc tabulate data=dig noseps formchar=' __________' missing;
 class trtmt cvd whf vena sva dig mi uang strk crev rinf oth hosp;
 format cvd incr. whf incr. vena incr. sva incr. dig incr. mi incr. uang incr. 
   strk incr. crev incr. rinf incr. oth incr. hosp incr. trtmt trtr.;
 tables cvd whf vena sva dig mi uang strk crev oth rinf hosp,
      trtmt*((N *f=8.0) (colpctn *f=8.1))
            /condense rtspace=42 box='Proportions: DIG Trial Table 3';
run;


proc tabulate data=dig noseps formchar=' __________' missing;
 class trtmt dwhf ejfgrp diguse cause ctratio nyhagrp;
 format trtmt trtr. dwhf incr. ejfgrp ejfr. diguse yesno.
   cause causer. ctratio chestr. nyhagrp funct2r.;
 tables ejfgrp diguse cause ctratio nyhagrp,
      trtmt*dwhf*((N *f=7.0) (pctn<dwhf> *f=7.1))
            /condense rtspace=32 box='Proportions: DIG Trial Table 4';
run;

* PRINT A TABLE OF RR FROM COX MODELS (NEJM TABLE 3);

proc datasets nolist; delete all;run; *removes dataset if it already exists. This statement must be executed if re-running program;

*Below is Macro to calculate HRRs found in table 3. Note some HRR are different from manuscript due to combining certain outcomes;
%macro tab3(var, vardays);

* proportional hazards model. output dataset has 2 obs: beta coefficient and variance of beta;
proc phreg data=dig noprint outest=phout covout;
    model &vardays*&var(0)=trtmt;
    run;

proc transpose data=phout out=out prefix=beta; var trtmt; *put beta coeff and var on same row;
data out; set out;
 outcome="&var  ";
 HRR=exp(beta1);                    *hazard rate ratio;
 waldx2=(beta1/sqrt(beta2))**2;     *wald chi square statistic;
 pvalue=1-probchi(waldx2,1);        *P-value ;
 ll=exp(beta1-(1.96*sqrt(beta2)));  *lower limit of HRR;
 ul=exp(beta1+(1.96*sqrt(beta2)));  *upper limit of HRR;

proc append base=all data=out force;run;
%mend;

%tab3(cvd, cvddays);
%tab3(whf, whfdays);
%tab3(vena, venadays);
%tab3(sva, svadays);
%tab3(dig, digdays);
%tab3(mi, midays);
%tab3(uang, uangdays);
%tab3(strk, strkdays);
%tab3(crev, crevdays);
%tab3(ocvd, ocvddays);
%tab3(rinf, rinfdays);
%tab3(oth, othdays);
%tab3(hosp, hospdays);

proc print data=all;
 Title 'HRR for NEJM Table 3';
 var outcome hrr waldx2 pvalue ll ul;run;


* PRINT A TABLE OF RR FROM COX MODELS (NEJM TABLE 4);

*Create interaction terms. Considering treatment and covariate as dichotomous
groups, interaction term is where treatment=digoxin and covariate is at high risk level;

data dig; set dig;
 if 0<ejf_per<25 then ejfgrp=1; if 25<=ejf_per<=45 then ejfgrp=0;
 if diguse=1 then prevdig=0; if diguse=0 then prevdig=1;
 if chfetiol=1 then cause=0; if chfetiol>1 then cause=1;
 if 0<chestx<=0.55 then ctratio=0; if chestx>0.55 then ctratio=1;
 if functcls in(1,2) then NYHAgrp=0; if functcls in(3,4) then nyhagrp=1;

 ejfint=ejfgrp*trtmt; digint=prevdig*trtmt; chfint=cause*trtmt;
 ctint=ctratio*trtmt; nyhaint=nyhagrp*trtmt;


proc datasets nolist; delete all2;run; 
*removes dataset if it already exists. This statement must be executed if re-running program;


*Below is Macro to calculate HRRs found in table 4;
%macro tab4(var, int, label1, label2);

* proportional hazards model. output dataset has 4 obs: 1 row for beta coefficients and 3 rows for var-covar matrix;
proc phreg data=dig noprint outest=phout covout;
    model dwhfdays*dwhf(0)=trtmt &var &int;
    run;

* Manipulate output dataset so that dataset rows match table 4 rows for each variable;
data beta; set phout; if _type_='PARMS';int=&int;
data var1; set phout; if _type_='COV' and _name_='TRTMT';
 setrt=sqrt(trtmt); keep setrt _LNLIKE_;
data var2; set phout; if _type_='COV' and _name_="&int";
 seint=sqrt(&int); keep seint _LNLIKE_;
data covar; set phout; if _type_='COV' and _name_='TRTMT';
 covar=2*(&int); keep covar _LNLIKE_;
data row1; merge beta var1 ; by _LNLIKE_;row="&label1   "; keep row trtmt setrt;
data row2; merge beta var1 var2 covar; by _LNLIKE_;
  row="&label2   ";
  trtmt=trtmt+&int; setrt=sqrt(setrt**2+seint**2+covar);
  keep row trtmt setrt int seint;

* combine rows and calculate statistics of interest for each variable;
data out; set row1 row2;
 HRR=exp(trtmt);                    *hazard rate ratio;
 waldx2=(trtmt/setrt)**2;           *wald chi square statistic;
 pvalue=1-probchi(waldx2,1);        *P-value ;
 pvint =1-probchi((int/seint)**2,1);  *P-value for interaction ;
 ll=exp(trtmt-(1.96*setrt));        *lower limit of HRR;
 ul=exp(trtmt+(1.96*setrt));        *upper limit of HRR;
run;

proc append base=all2 data=out force;run;
%mend;



%tab4(ejfgrp, ejfint, EJF25_45, EJFLT25);
%tab4(prevdig, digint, PRIORDIG, NOPRIORDIG);
%tab4(cause, chfint, ISCHEMIC, NONISCHEMC);
%tab4(ctratio, ctint, CTRATLE55,CTRATGT55 );
%tab4(nyhagrp, nyhaint, NYHA1OR2, NYHA3OR4);


proc print data=all2;
 Title 'HRR for NEJM Table 4';
 var row hrr waldx2 pvalue ll ul pvint;run;


