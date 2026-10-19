"""Import only selected public illustrations and verified inspection media."""
import argparse,json,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser();parser.add_argument('--game-root',type=Path,required=True)
GAME=parser.parse_args().game_root.resolve()
items={
 'concept':('art/generated/creepy-cute-thumbnail-v1.png','Conceptart · AI-illustratie','Promotionele conceptillustratie van de rozentuin met Bunix, Bunny en Critter.','concept'),
 'rose-models':('art/previews/scenery-v4/roses-detail.png','Blender-render · modellen in ontwikkeling','Nieuw gemodelleerde rozen met overlappende blaadjes en een rank met bladeren.','render'),
 'architecture-models':('art/previews/scenery-v4/architecture-detail.png','Blender-render · modellen in ontwikkeling','Een verweerde stenen boog, ruïnepijler, ijzeren lantaarn en draadspoel.','render'),
 'character-render':('art/previews/characters-v3/front.webp','Blender-render · personageontwerp','De eigen modellen van Bunix, zittende Bunny en de ronde wollige Critter.','render'),
 'character-native':('art/previews/characters-v3/native/restore_three_quarter.webp','Roblox Studio · personage-inspectie 0.3.1','De drie stoffen vrienden tijdens een native inspectie van hun beweging.','native'),
 'chapter-one':('art/previews/native-gameplay-v18.png','Roblox Studio · historisch spelbeeld, versie 18','De eerste route door de zwevende tuin in Roblox Studio.','native')}
items.update({
 'rose-native':('art/previews/scenery-v4/native/rose_detail.png','Roblox Studio · decorinspectie, nog niet uitgebracht','Gelaagde roze rozen met groene bladeren tijdens de decorinspectie in Studio.','native'),
 'harp-native':('art/previews/scenery-v4/native/harp_detail.png','Roblox Studio · decorinspectie, nog niet uitgebracht','Een houten dauwharp naast rozen, verweerde steen en de lichtgevende route.','native')})
media={}
for key,(relative,label,alt,kind) in items.items():
 source=GAME/relative;target=ROOT/'public/assets/media'/(key+'.webp')
 assert source.is_file(),source
 subprocess.run(['magick',str(source),'-resize','1600x>','-strip','-quality','86',str(target)],check=True)
 w,h=map(int,subprocess.check_output(['identify','-format','%w %h',str(target)],text=True).split())
 media[key]={'file':target.name,'width':w,'height':h,'label':label,'alt':alt,'kind':kind}
subprocess.run(['magick',str(GAME/'art/generated/creepy-cute-icon-v1.png'),'-resize','96x96','-strip',str(ROOT/'public/assets/icon.png')],check=True)
(ROOT/'content/media.json').write_text(json.dumps(media,ensure_ascii=False,indent=2)+'\n')
print('Selected media prepared:',len(media))
