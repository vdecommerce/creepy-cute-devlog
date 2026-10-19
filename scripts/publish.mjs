// Publish generated files only. Never reuse a user's working directory as staging.
import {spawnSync} from 'node:child_process';import {mkdtemp,cp,rm} from 'node:fs/promises';import os from 'node:os';import path from 'node:path';
const root=path.resolve(import.meta.dirname,'..');
function run(args,cwd=root,allowed=[0]){const r=spawnSync(args[0],args.slice(1),{cwd,encoding:'utf8'});if(!allowed.includes(r.status))throw Error(args.join(' ')+': '+r.stderr);return r.stdout.trim();}
if(run(['git','branch','--show-current'])!=='main')throw Error('Publish reviewed main only');if(run(['git','status','--porcelain']))throw Error('Preserve local changes before publishing');
run(['git','pull','--ff-only']);const source=run(['git','rev-parse','HEAD']);run(['npm','run','build']);run(['npm','run','check']);
const remote=run(['git','remote','get-url','origin']);if(remote!=='https://github.com/vdecommerce/creepy-cute-devlog.git')throw Error('Unexpected publish repository');
const temporary=await mkdtemp(path.join(os.tmpdir(),'creepy-cute-pages-'));
try{run(['git','init','-b','gh-pages'],temporary);run(['git','config','user.name',run(['git','config','user.name'])],temporary);run(['git','config','user.email',run(['git','config','user.email'])],temporary);run(['git','remote','add','origin',remote],temporary);
 const fetch=spawnSync('git',['fetch','--depth=1','origin','gh-pages'],{cwd:temporary,encoding:'utf8'});
 if(fetch.status===0){run(['git','checkout','-B','gh-pages','FETCH_HEAD'],temporary);run(['git','rm','-r','--ignore-unmatch','.'],temporary);}else if(!/couldn.t find remote ref gh-pages/i.test(fetch.stderr))throw Error(fetch.stderr);
 await cp(path.join(root,'dist'),temporary,{recursive:true});run(['git','add','--all'],temporary);const difference=spawnSync('git',['diff','--cached','--quiet'],{cwd:temporary});
 if(difference.status===1){run(['git','commit','-m','Publish site from '+source.slice(0,12)],temporary);run(['git','push','origin','HEAD:gh-pages'],temporary);}else if(difference.status!==0)throw Error('Could not inspect staged publication');
 console.log('Published generated site to gh-pages from '+source);
}finally{await rm(temporary,{recursive:true,force:true});}
