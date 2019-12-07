from typing import List
import itertools
import collections


# class DSU:
#     def __init__(self, N):
#         self.par = list(range(N))
#     def find(self, x):
#         if self.par[x] != x:
#             self.par[x] = self.find(self.par[x])
#         return self.par[x]
#     def union(self, x, y):
#         self.par[self.find(x)] = self.find(y)


# class Solution:
#     def numSimilarGroups(self, A: List[str]) -> int: # (NW) * min(N, W*W) complexity
#         N, W = len(A), len(A[0])

#         def similar(word1, word2):
#             diff = 0
#             for x, y in zip(word1, word2):
#                 if x != y:
#                     diff += 1
#             return diff <= 2

#         dsu = DSU(N)

#         if N < W*W: # If few words, then check for pairwise similarity: O(N^2 W)
#             for (i1, word1), (i2, word2) in itertools.combinations(enumerate(A), 2):
#                 if similar(word1, word2):
#                     dsu.union(i1, i2)

#         else: # If short words, check all neighbors: O(N W^3)
#             buckets = collections.defaultdict(set)
#             for i, word in enumerate(A):
#                 L = list(word)
#                 for j0, j1 in itertools.combinations(range(W), 2):
#                     L[j0], L[j1] = L[j1], L[j0]
#                     buckets["".join(L)].add(i)
#                     L[j0], L[j1] = L[j1], L[j0]

#             for i1, word in enumerate(A):
#                 for i2 in buckets[word]:
#                     dsu.union(i1, i2)

#         return sum(dsu.par[x] == x for x in range(N))


class Solution:
    def numSimilarGroups(self, A: List[str]) -> int:
        n, ds = len(A), DS()

        for i in range(n):
            if not ds.has_parent(i): ds.set_parent(i)
            for j in range(i + 1, n):
                if not ds.has_parent(j): ds.set_parent(j)
                if self.is_similar(A[i], A[j]): ds.union(i, j)

        return ds.count

    def is_similar(self, a, b):
        return len(list(filter(lambda i: a[i] != b[i], range(len(a))))) in (0, 2)


class DS:
    def __init__(self):
        self.parent = {}
        self.rank = {}
        self.count = 0

    def find(self, x):
        if x != self.parent[x]: self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def has_parent(self, x):
        return x in self.parent

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py: return False

        if self.rank[px] > self.rank[py]:
            self.parent[py] = px
        elif self.rank[py] > self.rank[px]:
            self.parent[px] = py
        else:
            self.parent[py] = px
            self.rank[px] += 1

        self.count -= 1
        return True

    def set_parent(self, x):
        self.parent[x] = x
        self.rank[x] = 0
        self.count += 1



sol = Solution()
assert sol.numSimilarGroups(["tars", "rats", "arts", "star"]) == 2
assert sol.numSimilarGroups([
    "vokibbzcxg","ibbzgxvock","gczbbvxkoi","kzboixbvgc","igzcbkovxb","boczkxvbgi","zcgkbobixv","igzovcxbkb","zxkbvgcobi","oxbzkbicgv","obzvixckgb","gzcbovxibk","ibbocgzkvx","oibbzvxgkc",
    "bcoxibzkgv","xkgbzbociv","gvobikxczb","vkzixgbbco","igxzkbbvoc","vkgxozbcib","xgvbczboki","ogizbxcbvk","kbxcizvbog","zcobkvxbig","zbvikobgxc","cizkbgovbx","zcbvxkboig","zogbbkxciv",
    "czigoxbbvk","gobkvczibx","kcviogxbzb","ixkvbogzcb","goivbbkxcz","bzcovbgikx","zbogxvkcbi","obkvixczgb","xzbivokbgc","vkxzbibgoc","zkixgovbbc","bvgxczokbi","vbboxckgzi",
    "obigkcvxzb","okicbbxgvz","zxogvkbcbi","zkgcobvibx","zokbibcxgv","kbvzcbgxio","bkgvxobizc","bgboxvikcz","bikgzbocvx","gbbixzcovk","ivgbbozcxk","bxocvkibzg","bcixkgobvz","gxokvizbcb","zioxvcbbgk",
    "vkzoxcgibb","zgkiocvxbb","czvobgbkix","gbvizkboxc","cbzgixobkv","ixcvkbzgbo","ovgbbikczx","bgibkxozvc","obbizvxgkc","gvzckbxobi","kbvozgcxib","czbvbikogx","cbixgzobvk","zbogckvxib","kvobgixzcb",
    "xovzibbgkc","xbibvkgcoz","bxgvkobizc","gzbvxikcob","xzgcvikbob","gbziovkbcx","bgxibckzov","kbgvcixzbo","ibvgokcxbz","oxvkicbzbg","zxbcvgkbio","ovkzigbcxb","kvizbxbcgo","gbcxboikvz","cvkozgixbb",
    "xcgkvbizob","kgxbzvbcio","kgcoxbbvzi","cigvxbkozb","kbocgxzvbi","kcgobxbizv","iockgvbbzx","cvzibboxkg","cbixgzvbok","kbgzicbxov","gbkbxzcoiv","cixgbzkobv","ckgbzvixbo","gzkbcxibov","bcbkigzoxv",
    "zkibvbcgxo","zcgokxivbb","bxbkvizgco","gxkzboivcb","ovibcxbzkg","kobbzcvxgi","obcvibkgzx","czkbgibxov","xbibcgvkoz","gbiobckxvz","vozgkbbicx","bgocvxibzk","xvkgobbicz","kvcgbbozxi","obcbkvxgiz",
    "bkgbozvixc","gkcixbvobz","xcvibzkbog","xvcbbogzik","kbizbcoxvg","bbvxkgcioz","cbzvkxbgio","gozbvcxkib","bzbvkioxcg","kgxcobvbiz","ovkbxgczbi","ziocxbgkbv",
    "ovgkixbzbc","zbcbvgoikx","vbbczgioxk","kbogxzivbc","zkbbicxvog","izboxvcgkb","gxvizocbbk","bgizokbcvx","vgbcobkixz","ivbxzobcgk","bgvzoikcxb","bkbozgvxic","ikovgcbzxb","obxbgvczik","bziobcxkgv",
    "kvbcbzixog","bbocxvigzk","vibgzcxkbo","gciovxzbbk","ozcbibgkvx","cibxbgvzok","zbkgbxcoiv","xibbczogkv","bviobkczgx","bovkixcgzb","vgbczxboik","bzgkbvoixc","ixbozvkcgb","bkxogvcizb","vbkoxcgibz",
    "bivkxbgczo","zvgocxbbki","bokbxzvgci","gzxiobcbvk","bvcgxobzki","gikbbzxcvo","cbzvixbgok","obgbzkixcv","bcbvgxkzio","vbcbikzxgo","zcvbxkboig","bxzgbcvkoi","ikxcgbozbv","ovixgzcbkb","zocbibgkxv",
    "vzgibokcbx","izxgkcbovb","bkxiogvbcz","xcigkvobbz","ikbxzvcbgo","vbcbxzoikg","bcigbkovxz","obvbxigczk","gxbvikczob","cxizbgkobv","vkbocixbgz","ibbzgcovkx","ibkgvcxobz","kbicgzobxv","bicvgxkzbo",
    "bxozgbvick","xibbgovczk","cxvobbgkiz","bxkzbgiocv","bvoxizbgck","bzvxobigck","gbxvczkboi","bgoxzcvbki","bgkbvizxco","xbkoczgivb","xgiozkbcvb","zobgxkvbci","bckvzxiogb","gbixzvbkoc","vxgbizobck",
    "xzcbogbvik","bvxbzciokg","oxvgbczikb","vizcxgokbb","zgxibkocvb","covkbixzgb","bkbxzvcigo","cxzbigbovk","oxzcvkigbb","kbobgixczv","cgxoibkbzv","xbgbzkociv","bocxbvzigk","cgzoivbbxk","cobzkxgvib",
    "gxbvibkzoc","zxgvicbkbo","xvzkbiocgb","bcgbivoxkz","gobbxcvzik","zckiogbxbv","ocgizxbkbv","gibxzcokvb","vgcobixkzb","kxozgbvicb","xcgbizobvk","zkbgicoxvb","ibogxkbvzc","cogzxbkvib","kigbvcoxzb",
    "vbicoxbkzg","vkzcgxobib","gicvbxzbok","gzkcbviobx","bbzxogkcvi","bxibczvgko","ivbkbxzogc","ibvkoxbzgc","bzxcvgobik","iokgxbbzcv","oibkvcxzbg","bkxgbvzico","bocixkgzvb","kcigbzvxbo","ibocgbzkxv",
    "xbovcgikzb","gcziovbxbk","cxgbizobvk","bgcokbivxz","bockgvibzx","bvzboxkgic","obckbxzivg","bocizgvxkb","czbvbkgoix","oxvbbkczig","bkgzbovixc","bzixkcovbg","civkbxbogz","zckbobvgix","bvxgicbzko",
    "kbxizvbogc","ozbixvgckb","kxcbzogbiv","xgvibkczob","vxocikbzbg","bkvigbczox","bzikgcxobv","gbxovzicbk","xcgbizovbk","ocxzbigvbk","kzxbobigvc","gckovxzbbi","xzgbkiovcb","ckzbigbovx","cokgxzbbiv",
    "vbxgczkboi","vkzixbgobc","gcxbbvzkoi","ogvczibxbk","kbbzcvixgo","cixkgobbvz","bkxgvzobci","bvgkcxbzoi","bxovbzkgic","bkbzicxvog","vibbzcgkox","kcbvzgioxb","cbbkioxzgv","xgkzbviobc","vgoicbkbxz",
    "izbbvgxcko","ivbkgxcozb","cgvibkxzob","bbkcovzixg","bkgcobvizx","vobxcgkzbi","vgbcbkixzo","vgixbzkboc","bxbkigzvco","bkizbgxovc","bbkgioxvcz","ovkbczixbg","gikobzvxcb","ozxcgvkbbi","gvizbxbcko",
    "xkicbbogvz","xcgoizbvbk","gicbvxzbok","kbibxzvogc","cbzgixovbk","koizbxvcbg","oizgbbxkvc","gibbvzkoxc","gxvizockbb","kivczgboxb","zvbicgkxob","igcbbzxokv","cgzbvxboki","kbcgzxbvoi","ockbgixbzv",
    "gibzckbovx","gkvxbbcizo","ocbzivxkbg","gikobzxvcb","kbvxzgcoib","vcobxgkibz","bzcxogbvik","bxbzigkvco","gbbovzicxk","cgixbzobvk","kgibzxbcvo","czvxbgboik","gzbixcobvk","gkbvbcioxz","gxvbbckozi",
    "vozgkbxicb","bgbivzkxco","xzbvcbigko","cgkibbxzvo","ocgixbzbkv","xbogkcvbzi","vkgixzbboc","cogbxbzikv","bkcgbioxzv","cikgbzxobv","kbocvgxibz","izbxvokgbc","xckobigzvb","zibkbogcvx","vzkbcigobx",
    "bbvoxgcikz","obcbkxvgzi","kxoibbgcvz","bzkxovigbc","icbkbgzoxv","ixokvbzcbg","ivbkoxzbgc","kbxcizvgbo","cokixzbbgv","vbkbzigoxc","izckxvgbbo","kcvbixgbzo","bcbxiozkgv","ogzxkivbbc","cbgzvboxki",
    "ozbcbxkgiv","vobzgibkcx","okzbvgibcx","gbbxcoikvz","xkzbbgvioc","bibzxgkvco","bzvocigxkb","ibovkbgcxz","cxzobgbkvi","gxokbvizbc","ibbzgcokvx","zxiogkbvbc","cbvkibgzox","ogizbxcbkv","xvgoczbbki",
    "kbiozgcxvb","zxkciogvbb","vkxgczbiob","kgbizvobxc","gobkvczxbi","vkiocbbzxg","vobkigxzbc","bvxgicbokz","czvxbgbkio","voxcikbgbz","ogkzxibvbc","iockgbbvzx","bxozgkibcv","gxbvickzob","zgkvbobicx",
    "bvzboxkcig","zckbvgxobi","ogxvbcizbk","cobzibxkgv","zigboxcvbk","bzckboxgiv","vgcibkbxzo","xoibvcgkzb","zgxvbcoibk","vkoicbgbxz","bcvzokbigx","oiczkgbxbv","xizocbvgbk","xibbczkgov","cgiobzkbxv",
    "vbioxzgbck","bczvxokgbi","viboxckgzb","gxzckbiobv","xikbgovczb","cxiogzkbbv","xibgbzvcok","vgbxzoibck","zivkbbgcxo","bbgiockxzv","bvizgkboxc","iobbzcvgxk","gxbvkiczob","vbcbkigzxo","boibzgcxkv",
    "zkbgbxcivo","bzvcixbgko","cvkbozgibx","xbckzgiobv","bxcvgikzbo","zckoigbxbv","bgzxckbivo","bxiogzcvkb","ibbvgxzock","bbcvigxozk","kzicxbgovb","cgbobvxzki","czbovbxgik","ibkvoxbcgz","kbbxiogcvz",
    "xvckbogzib","kgxbivoczb","bgxkvcbzoi","kivzogxbbc","oxvgbcbizk","xkvbbocizg","vgxkbczbio","gikxbzovcb","zokbbicxgv","ikxbzvcogb","xgizokbcvb","oikxcbbzvg","zgcvxkobbi","civkbxbozg","ovcgkbzibx",
    "izxbbkgocv","xbckoibgvz","vozgxbbick","xzcvogbbik","bcikzgvobx","ikvcxzogbb","bgvcioxzkb","gozbcivxkb","gkioxczbbv",
    "bcgioxkbzv","zbogxbkcvi","cbzikxbgvo","cbibogzvkx","xgovibbkcz","ikvgbocbxz","ocgbxbzikv","gvokcxizbb","kbxiovcgzb","icokbbzgxv","bkvgocbixz","bibkocgvxz","xkozibbvgc",
    "cvxgbbokiz","vkobzibgxc","vxizbokcbg","gicbkzxbov","vobzigbkcx","kzbxbogciv","ogvbxizckb","zbxiobgcvk","gcboxbkziv","kgibxczbvo","vcbxozbkgi","vbioxgzbck","kzgibovcbx","bkxgbvcizo","zvxkibcbgo",
    "gkobxzivcb","oibvxczbkg","gizbcvxbko","bvkoxzcbgi","bzvxbgocik",
    "igcbbzxvko","gxvicozkbb","bxbvkiogcz","bkcgbxoizv","zibgovbxck","bzvocigbkx","obcbkigzxv","ozvibbckxg","vxkgczbiob","bozbgvkcxi","cbxgzkvoib","ziobvcbxgk","gobcvixzkb","cbzgixovkb","ivcxzkbbgo",
    "kbcviogbxz","viokczgbbx","cbzvixbgko","cxzbogbkvi","ixzvkgcbbo","igobbzxvck","vzbxgoibck","bzcogikbvx","koixbgzbcv",
    "cibzvbkxog","bbziogxkcv","kcogzivxbb","bgvcixbzko","bvoczikbgx","bgikzxbcvo","obxbkcizvg","zcbvkxboig","bxcbvzogki","ozgbvckbxi","bgizxbcokv","xbizgcvbko","vckzgiboxb","xzobkcvgbi","zgvcxkobbi",
    "vkibgoxzbc","zxkovcgbib","bxozvkibcg","bxbkivzgco",
    "ozvkxbigbc","xkvcbgzboi","bobizgkcxv","obkgibzcxv","bcoxbgkziv","cizgbbxkvo","igzovbxbkc","bvzocbkgxi","bbzkiovxcg","xibozbcgkv","kbzvcixgbo","gkixovbzcb","zoicbbgkxv","vgbxczokbi","zobkibcgxv",
    "obkgbcvzxi","bboizgxkcv","ocxibzvbgk","gxvockbzbi","bbzcvikogx","cbvkiobzgx","vxgbcbzkio","kgxbicovzb","bcvkizgbxo","vigoxbkczb","cxzbibgovk","zxkvbgcboi","cvgzkbxibo","ckivbbgoxz","kgzbivocxb",
    "gbvobzicxk","vbgxbzoick","vciboxkzbg","xgzbkbcivo","ckgvibobxz","iboxvgzkcb","gxbkbcvozi","zxbocbkvgi","cbzkogbvxi","zkvbxocbgi","kbvzocxbig","zbcxgbkoiv","ovicgzxbkb","zobkxgvbci","gkbocxbvzi",
    "kvbgzcxibo","ovczigbkxb","xizvbkocgb","zbcbikvxgo","cgozbbvikx","izkbcbvgox","igobbvxzck","vbzxickbgo","igbvkzxbco","vxizbgobkc","kcozgivxbb","gvbxczokbi","vxbiobzkcg","zvgbkbcxio","bgbzivkxco",
    "bvoczgibxk","ivbzgxbkoc","xcvobigzkb","bzvcixogkb","bvixkgzbco","bbzxcgkivo","bcbigzxvok","ivgczbbkox","vkobcizbgx","xogcvikzbb","zckbvgxboi","gkbzbovixc","xcgkibvzob","kxbogczivb","gvbizkboxc",
    "xvkgbcozib","izcvogbbxk","xgvikozcbb","ozcgbxbivk","bogicvzbxk","xbvkiocgzb","kcvbozxigb","obvbzgixkc","ivogbzbckx","zgiocbvbkx","cbovixbgzk","zbgkixobvc","kzbxbvicgo","ogzibxcvbk","zkoxvicbbg",
    "xkogzivcbb","zbckvxbgoi","xbzickogvb","kzbgbovxci","gozbcibxkv","ozcxvbgkib","xzcbvbokgi","vokibbxczg","kvbiobgcxz","xvibcgbkoz","vkxbiobgzc","xbikgcozbv","bkgzbvoixc","bckbxzvigo","bovczikbgx",
    "kcvoixgbzb","vobbkgzxci","gkbibocvzx","igkcxvbozb","ocvzigbkxb","vgiobzkbxc","xbizbogvck","xzbickogvb","bkxcgbvizo","xczbkbgvio","zcokbvxbig","vbizcxkbgo","zikxcbvobg","obcbxkvgzi","xczbbkgvio",
    "ibbcoxgkzv","bcoxzgvbki","cgobzbxvik","icbovgbxzk","kbbxcozgiv","xgozbvikbc","xboigzckvb","ovzbgkxcib","bbxkgzcvoi","bxicvkbgoz","vcxikbbzog","kbgxcobivz","ozcxibgkvb","bzxbovgcik","bgoizkbcxv",
    "kxcovibzbg","gizxokvcbb","zivxgcbkob","ibovgkzcbx","kzboivgcxb","zkvbxogbci","kbgvzxbcoi","zxkvbgcobi","kxoizbbvcg","xvzobcibgk","xvgzkicbob","vcbzoxbkgi","xbkgibczov","bzigvkboxc","gvbxckbzoi",
    "kiocbgbvxz","vckibgzobx","vkbxzoibcg","iokzbxvcbg","ovgixzckbb","ibvzkobgxc","vikbczboxg","zkgviocxbb","obgkbcvzxi","vgkixzbboc","bzokbcgivx","kzbxbvgcio","ikbcgxobzv","vzobcigkbx","oxbkvibgcz",
    "igxocbkbzv","bbvgokcxiz","ixkzbogvbc","cvxgbzokib","zvicbgxbko","kgbvxcbioz","ibcgzbxkvo","vzbckgxoib","izxbkbvocg","xogbzvkibc","xgbvkcibzo","vcxbkbizog","ogzvxbbkci","bgbkvizxco","xvcibobgkz",
    "vxbzbkicgo","zkvbbocigx","kgiovxcbzb","bczgioxbkv", "obcbgikzxv","xbvgkcobzi","xbcvbigozk","oizgbbckvx","cboxvgzkib","givoxcbbzk",
    "bvgxcbokzi","bvoxbgzcik","cvgzxokbbi","bgobikzxcv","kgozxbivbc","cibkvxozbg","zocgxkvbbi","xibbzocgkv","bogcivbkzx","ozbcbgxikv","xivbbzkgco","vxkzobibcg","xcvbizkbog","bvkgbcxoiz","oxikvczbgb",
    "ocgikbzbxv","cxbzgbkovi","xzbivkobgc","gobkvzcxbi","ocxibbvzgk","bkcobxgizv","ibkgboxvcz","gxkzboivbc","kzgibcxobv","bcovikgxzb","kixcvzbgbo","gbovbxckzi","bibocgzkvx","zogckxbvib","xiovbzkgbc",
    "bovcigbkzx","kxcovibbzg","ckioxzbbgv","bviobkxzgc","bkbcigzoxv","iocbgkbvzx",
    "igkcxzbovb","bovgzikbcx","xkzbgvocib","oxbzgckivb","zxbocbgvki","zcobbvxkig","xvkgzbboci","cgovbixzbk","ogcixbvzbk","cgozbixkbv","cbzbixvgko","gbikozcbxv","obzxcigbkv","oxbkicgbvz","ckzibgbovx",
    "bvzogkxcib","zxvickgbob","ickzbxbvgo","czbgxoivkb","ixkvbozgcb","gobivcxzkb","obixgkcbvz","czbiogxkvb","zkvcgxbbio","zibgoxbvck","zbicgkvbox","bzicbgoxvk","bbvkxgcioz","kbvzgbxoci","gxoizvckbb",
    "bcxgvzobki","cxgzobkvib","gibxvzobkc","iboxbgzkcv","kgbvxbczoi","kzboivbxgc","kvoxgbizcb","kbogvcxibz",
    "bcovikzxgb","zkgvxocibb","zbgbikxovc","bzoxcivbkg","gbikozbcxv","bzivcgobxk","oibgxckvzb","bogzicvkbx","bbzkiovxgc","gibovxcbkz","izxbgbokvc","czbgxkivob","cigzxbkvob","vobbkzgixc","cvogbixzbk",
    "oxibcvbzkg","zgoxbvcbik","bozxgbcikv","kgzivcbbxo","xzivgobbck","bkzxcgbivo","xbzbgcivko","gxokivzbcb","czbgoxibvk","vikbxbczog","bibzckgovx","ozxbigcbkv","ozcxgvkibb","xzbicovgkb","kbgviboxzc",
    "ikzcbgbovx","zbkgcxboiv","icbkvgbxzo","kbzgxiovbc","xgbbcovizk","kgocibbxvz","kgiocxvbzb","boixvbgzck","gozbkvbxic","vkxciozgbb","xbicbgvkoz","zbikbogcvx","ixzvkgobbc","kbvzogxbic","bozcvikbgx",
    "ogkzxbivbc","bcobikzxgv","kcoixgbvbz","bbvixgcokz","vxikbgbzco","xbgibvcokz","bxokcbgviz","obikxgbcvz","oxikgvzbcb","kobvxcbigz","igzcbkbvxo","gzxkobvicb","kigbcbxozv","boczkxvbig","vzbckxgoib","obcbkvxgzi",
    "bgoxbvczik","iczbbgkvxo","kgzbxovcib","kibxozcbvg","bkxbicozvg","bibxcgvokz","bibxgcvkoz","izbovxkgbc","xcbkzgvboi","ozbcvxkigb","ibvoczxkbg","icxgbbzvok","xzkgcbviob","vxzobcibkg","koxgvcbbiz",
    "xkzciovbgb","kbgbixozvc","bxgkvcbzoi","xzivgbbock","coibxgbvzk","cibzxbkvog","gzkbcxiobv","kbvzbcgxio","xbzickgovb","zxkciobvgb","vcxgikzobb","ozkbcvbxig","cgioxzkbbv","obvbkxgizc","kbbcvzixog","cibobgzkvx",
    "bgbizvkxco","kbvzbcoxig","kcoixbbvgz","bxckizvbgo","biocvxgbzk","kibcgxobzv","kgiczboxvb","bkigzxbovc","bkicxgovzb","zbovkcxibg","boixczgvbk","bcxibvkzog","bizxkcovbg","ixckvzbgob","bzxckiovbg",
    "cbkgoxzbiv","bogbczvxik","cikgbvxobz","zibgkoxvcb","cibgvzbkxo","bvoibkxzgc","xbkzogcbvi","izbxovcgkb","ckgozbivbx","bkvgicbzxo","vzgibobckx","cxzobvibkg","bzkoxvigbc","gbxiobcvzk","cxzoivbkbg","cozbbvxgik",
    "okzbvcibgx","zickxvgbbo","igbozvcxbk","zivxbkbogc","oviczgxbkb","bvibzgxcko","gxizkbcobv","zbikgcoxbv","gkicxvbobz","gbxvobcizk","kcizbxbvgo","izbkcgobvx","bovzigbkcx","kbigbzvxco","bkxgovcizb",
    "bxkgibzovc","zbcxgokbiv","oxvbzcibkg","vgbbkozxci","kocbvxzibg","cxbizogvkb","vbcxkbgioz","gbvocxzibk","bzxbvgocik","gbikbzocxv","bkoigbczvx","icgbxzkovb","gcizbbkvxo","cizvxgokbb","zobbkicxgv","bvoxigbzck",
    "gxvobkczbi","bkcobxvigz","bzkcgobixv","zxkvicbgbo","xciogzbbvk","ovgkizbxbc","okbiczxvbg","bcgixbovkz","boizcbgkxv","cxikobvbzg","bzcbovgxik","vcobbgkixz","vbogbxkicz","vxbzikgobc","vzkboicbgx",
    "cbbkiovzgx","vxbcikgobz","obkcigxbzv","ockzbigvbx","vikbczobxg","cvbzgbkoxi","vzbckxgbio","vbxkiozbcg","xogcvikbzb","vxzgbcbkoi","kbbzocvgix","xkvbgizboc","zkcgbxboiv","xckzogbbvi","bkzbvcogxi","kvbiozgcxb",
    "xogvbzcbik","cixgzkvobb","cgzibbxkvo","xbigkvozbc","kcxbvzgboi","vzbckxbgio","bxocgikzbv","kobvxcibgz","zvcikxgbbo","bvizckgoxb","zxgkbcivob","ikogzxvcbb","gickovbzbx","bcxgikzobv","gibbovzcxk",
    "bcixkbogvz","bgkxizvboc","gobxcibvzk","goivbcbkxz","bibkogcvxz","gbvcxzoibk","ixzbcbgovk","ovizkgbxbc","obckizvgbx","bvczobkigx","cbxizbogkv","gbbocxkvzi","ibogxkvbcz","vixbckobgz","oxzcvkibbg","bbgxzciovk",
    "zbgbixkovc","ozbxgvibck","bcgokbivxz","obivkxzbcg","bbvzcigoxk","gcxizbokbv","bbkcovzgxi","bkvgiczoxb","obgbkxvizc","xgvicozkbb","cgibxzovbk","ikxcgbobzv","bkgczbvxoi","ibbvgxzkco","xobkzgvbci",
    "zbvkxogbci","xizvbkgcob","oikvxczbbg","zvkbcigobx","iozxbgckvb","bxcobvikzg","cioxbbzkgv","zivcgxbbko","xbzbogkcvi","cbkbgizxov","zvxgbcokib","cvoxbgzbik","bkgxovbciz","bgxvzckibo","vgizbxobkc","obizgkcbvx",
    "oickxvgbbz","bzcbxvgoik","xbgzbkiocv","bgvcibxzko","xckibgzobv","bvcbzoigkx","ozikcxgbvb","ozcixbvgbk","gkzcibbovx","zbikgocxvb","xvcbzbkgoi","cbvzgboxki","cxzvobkibg","ogzxcibbkv","cbiogzkbxv",
    "kibxovcbzg","xzckibgbvo","zxbgovckbi","xvckzigbob","icxkbbvzgo","vbgxzciobk","xbikgvozbc","zogbkxbvic","xzkicbvgob","ovbbixzgkc","bckxiogbzv","vxbbckiogz","oxvgbkbizc","igocbzxbkv","icvbgxkzob","zxbickgvob",
    "gxbkvobzci","cxbgozkvbi","bcxikvbzog","zxbogckivb","bizvcbxgko","kcbovgxzib","obcikvxgbz","cxbkozivbg","vboxbgkicz","zbgoxcivbk","kgbixcvobz","ikcxzvbbgo","bzvgbcioxk","vbgxobzkic","xzcoibkgbv",
    "oickzgbxbv","zbgbixokvc","igbzbkxcov","bbxkcovizg","bcvozkgbxi","kbbvczixgo","kivczobgxb","zbxbvokigc","cizvbgokbx","vzbbgokxic","bxivgzcokb","kbcbxvigzo","kzgixcbobv","kzxvobigbc","xgivzobbck","zivkxbgcbo",
    "ocizvkbbxg","ibovkcgbxz","gzivbcbkxo","vobxczgibk","kxvocgibbz","kxzivcbbgo","zbkgbxcivo","bkoigbczxv","ixbozbcgkv","bxcgvzobki","ixcovbbzgk","kgbvxbcioz","iogczvbxkb","oxbgickbvz","xkbbviozgc",
    "okibcxgzbv","xigckzbbov","bkgbzcvxoi","kvbxzcbogi","kxcizogvbb","xbgbciovkz","kvgbbozcxi","cvobixbgzk","vzibkbgcxo","kgvbcobzxi","cigzxkobbv","xbgibkcovz","gxovkbbciz","obzcvkigxb","ckovibbzgx","bvgzcxbiok",
    "xbvikocgzb","ovzikbcbxg","kbbvcixgzo","kcogzvixbb","bvzkobcigx","xibcozgkvb","okbbicxvzg","obvxkzgicb","bgkczxboiv","vobzgibxkc","kgvocxibbz","cbgobvxzki","gkziobcvxb","gibvxkzboc","bkvoixcgzb",
    "cokzivxbbg","vgbkioxzbc","vixbkbczog","vgbcbxoizk","ovibgcxkbz","bozcbigxkv","obxkigbcvz","zvcgbkbiox","vobzgxbikc","xkocgvibzb","ibkovxbcgz","bcoigxkbzv","czbgokvbix","zbgovcixbk","vxbzgkiobc","gixbckobvz",
    "ibcovxbzgk","gbivkxzbco","czvkbgboix","kcobvxbgiz","gxkobvczbi","ibxgobcvzk","ibbxgkvocz","xgbcozikvb","bxkcvbzgio","kobzivgxbc","ibgkzvcoxb","bxzgbcvkio","bcgoxbivkz","ibvcokbzgx","bczxobkvgi",
    "bozckxvbgi","vcxkbgzoib","vgicobkbxz","kocibxvbgz","bzcigokbvx","kcvobbxzig","zxbgcviokb",
    "vgiokzxbbc","vigbcbkxzo","oicgzbkvxb","gbvizxcobk","bcoibgkzxv","kboixcgvzb","ibvgczbxko","vgzckioxbb","gciovbzbxk","viboxgkczb","ixocvbzkbg","obvgbzcikx","kgicobzxvb","vkxicbgboz","xbgobivkcz",
    "ocbzibxkgv","xcobkzvgbi","ikvzogbcxb","bvxigcbzok","cvkoigzxbb","obicgzkbxv","cgobxzivbk","bkizbcxovg","cbbivxkzgo","vgkboczibx","obcvizkgbx","vkzixgbcbo","bcxozkgbvi","zkgvobcixb","gbvozxcibk",
    "ioczvbxgbk","vbbzgokxic","vbogkcxbzi","vbigxozbck","ozbxgkvbic","xcoibbkvgz","xbiobgvkcz","icgbxzokvb","iokxbzvcbg","cxbkozgvbi","gobivxcbkz","kibxbzgcov","vbckzxbgoi","xkzvbiocgb","oixgzkvcbb",
    "zgkixvbboc","bovkxbgczi","bxckzgvoib","givxkboczb","zgkbbcoxiv","kbvgcbzxio","zibgoxcvbk","gbckzxbvoi","cbxgkobziv","kvoigbxzcb","ckgbzbixov","bgxkvbiocz","kxocgbvizb","kzxigvcbbo","ozvbxbigkc",
    "bxizbckovg","cvgibkbxoz","bgxivcbzok","vcbgozbkxi","gbvkoxbzic","cxbizbogkv","zvxbckgboi","kxbogczvbi","bzoxcikbvg","kvgxbziocb","gkbxobivcz","bgzxicovbk","icvbxgkzob","zxboigcvbk","zkobvgixcb",
    "kxoibbczvg","bigbovzcxk","ixbvkgzboc","bkicxvgobz","bcgbiokvxz","kvbgcizoxb","xivogcbbzk","bgocvxkbzi","ibkvgozcbx","cigvbxzobk","bgvzkoibcx","vxkzcgibob","igvbczobkx","vikbzcgbox","kbobgvxczi",
    "okibcbgzxv","izxbgvcobk","kxzvobigbc","obvxbgkicz","kbcbxviozg","iboxckzgbv","vicogbxbzk","ivogbkbczx","givoxkbbzc","kcxbozivgb","bvkigxzobc","xkzvcigbob","kxocgvibzb","bixbkczovg","zkvcbbxogi",
    "vgkcobbixz","xzbbkiovcg","xoivbbzgck","vbkoxcigbz","bxcogikzbv","gcxivzobbk","xgobibzckv","vobzbcgkix","ibxgbocvzk","vkzixgbobc","kbvbgzxoci","bkzcxoivbg","izvoxgbkcb","bbvxgkozci","bvgkxcbzoi",
    "xbkgibzcov","bvkgocxbiz","vxkbbgcizo","bkicgbvxzo","bboixvcgzk","obgbcikzxv","kbocbgxivz","bzcxigkbvo","obizxckgvb","kobbvcizgx","kgibxczovb","gobcivbkzx","bcxzikgobv","cbgkxbvozi","zkocxvibbg",
    "kbbvocxgzi","zkbgcxbivo","gkibzxbovc","gzcobvxibk","kzcxgvoibb","gcozbbvikx","okvibbczxg","vobckigzbx","oxgkcvbzbi","gvizbxbokc","kbbzgvxoci","gkbzicobxv","gbxkvbiozc","bockzgvxib","gvozkicxbb",
    "vcbkzogixb","kibovcxgbz","cgioxbbvkz","igxbovzkbc","ckozibbvgx","bcbigzxovk","bzbiokxgcv","zixgkovcbb","bgcbizxvko","bxbkviogcz","zkgvixcobb","bvbgzoxkic","gikbbzxvco","kboigzvbxc","kxozcibvbg",
    "kgzicvbbox","ivkobzgcbx","igbvxbkocz","vkbgocbixz","gkbozbxvci","gibkvxcboz","zgbicvxbko","oxgzkcivbb","cbzvixogbk","vxzogcbkib",
    "ozvckbixgb","cvxkbgzoib","biovbzkgxc","kxbcigvboz","zbigcxbokv","vxboczgibk","gvokbxizbc","igbkvxcboz","xobvibzgck","vgoikzxbbc","kzbbvgcoix","xobbkgzvci","bkogzivcbx","bvxbzcigko","vcxkbgzbio",
    "kobxivcbzg","cibxbkvozg","vxzoicbkbg","gvbkcxbzoi","kibcgzvxob","kzgixvcbbo","cxbkboigvz","bvizgkcoxb","bbxkgzvcoi","oxbcvzkigb","vbbxckoigz","bozcvigbxk","ovbcbgxzik","xkigczbobv","zbobcvxkig",
    "bkzovgibcx","czbivbgkox","igobxvzkbc","zxcoigbvbk","ovgixkbzcb","kozbgvbxic","zbgbxcivok","obvbzgcxki","zxcgbvbiok","oxvkbibzcg",
    "bvcbzoixkg","zkvbbocixg","kcoigxbvbz","bbozvcigxk","kzbxbigcov","vzxkgciobb","ibvbgxzkco","cokbxzvgbi","cobkbxigvz","cizoxvbkbg","bbockvzixg","zbvogcixbk","xzcgbiovkb","zbgibkxovc","bzgvkioxcb",
    "obkbgixczv","obzxbgkicv","vogzbcbxik","vkzcgxbbio","cgzoxvbbik","bcgvioxbzk","cikbozgxvb","bizbcvxgko","vboixkbzgc","ocgzvbixkb","bgkocbxvzi","cvkgobxbiz","ibgobckxvz","ogibckzvbx","xcgbkvoibz",
    "bxbicgvzok","kxgbcovibz","obvcxgkibz","bxvcigbokz","gibcvxzbok","gbxoizvbkc","zbocxvibkg","kzvbbcioxg","ixvzkobgbc","xbziobgcvk",
    "bcoxkbigvz","zbbicgkxov","bxkvigozcb","ibogxkvzcb","ibcbkvgzxo","gkbbxcvzio","bvgizkboxc","kgvbxbczoi","bbxkzgvcoi","bivbzxkgco","boicbzgkxv","czixbgkobv","izbkcgbovx","ckoixzbbgv","gcboxivzbk",
    "bgizvbcokx","bckvzgioxb","kgbvzcioxb","kgbvcixbzo","kvbxzobcgi","bgkocbxizv","cxzbigbkvo","igxozkbcvb","xbkovcgibz","cioxvbzkgb","bkcivzogbx","vgzoikxbbc","cbivogzbkx","bxgbkozciv","kzvbocibxg",
    "vkibbxozcg","gkvbczxibo","gxoizvcbbk","xcoikbbvgz","ioxbzkvgcb","goxzkibcvb","cibbgxokvz","xckgvbiboz","iobzkxgvcb","cogkvbxzib",
    "oxbzcigkbv","czbvxbigko","zbgbxocivk","gocibxzvkb","kbvgcobzxi","bvogbkzxic","iovgkzxbbc","bvicbkozgx","kciovxgbzb","kibovgxzcb","kgicxbzovb","cbibxzovgk","xzoivbkbgc","icbkbozgxv","bkzcigbovx",
    "gobzkvbxic","ocgzbikvbx","obibgkcxvz","kbibxzovgc","kzbicovgxb","zocbbvkgix","kbogxizvbc","bzicvgoxbk","bgzkiovxcb","vobzbcgxik","vbizbgoxkc","ikvobzgcbx","bbizvkgcxo","bkxbzcigvo","ivcxbkzbgo",
    "ozkbcvixbg","xvgiozckbb","xbgikozvcb","bczibgkoxv","vbicbxokzg","cvbxozkgib","oizgbxckvb","zgbvoibxck","izxvgbokbc","gibovzxbkc",
    "vbcbxkzigo","vbizcxbgko","xkcvzigbob","gcziovkxbb","xzckivgbbo","kixgzovcbb","kbboczxgiv","ckbizoxbgv","igbxkzovcb","cbixvgzbko","vgixbzkbco","bogcxbzikv","xvkgzbbico","bzbvgoxcki","bvkbzgcxio",
    "bzvgbcxoik","xbibkvgzoc","cbbzioxkgv","xobbvgcikz","bzxvcogikb","bziokvcbgx","ikcvogxbbz",
    "xbckbgiozv","xkizobbvgc","izvcbxogkb","zkibxbogvc","coxbgibzvk","vgoxbbczik","bckiozxbvg","czovibbkgx","ibvbgxkzco","bxczvbogik","xbkogcivzb","cigkbzoxbv","bocgxivzbk","kgzbxovcbi","cboxvgikzb",
    "ibzgvobckx","gxvbockzib","cbgovbzxki","bzgckvxobi",
    "izxbbkvocg","kbzvobcgix","obbcixgkzv","zbckvobgxi","cigvbxozbk","kbbocxzgiv","xvcbbokzig","bizxgcovbk","zkgibovcxb","gokzbvibcx","kcvbizgbxo","oikbxcgbvz","zxkiogbcbv","cxkizogvbb","okbiczxbvg",
    "bobzgvcixk","zcivxobgbk","okxzbigcbv","vgibkbzcxo","ovibzgxckb","ogzvxkbbci","gikbczobxv","kxvbbcgozi","xzbickvgob","gzxbibcvko","gkxvobcizb","kvxibgzocb","cbxbgiozvk","kbbvoixgzc","givxbkoczb",
    "zgivbobkcx","bckoxbgizv","zxvkbcigob","bcizbgvxok","vgzkcboxbi","okgvibcbxz","bobizvkcxg","bobzkxgvic","vikbzobcxg","viboxkgbcz","kxoigbbcvz","goikcbxvzb","bkbgiczoxv","okvczbixgb","bvogxkzbic",
    "oigbcbxkzv","gkzoibcvxb","obzcxigbkv","cixbzovgbk","ikxogbcbzv","bcgokvzbxi","gcxobbkziv","bczxkgobvi","vbciogbzxk","ogixkzvbbc","vokzgibxbc","bxvciogzkb","zbiogkcbvx","igobzkbcxv","gzobvcxkib",
    "obvbxkgczi","bgczikvbox","zbvcgxbiko","ibxozkgcvb","xobbvkigzc","xvobcgbkiz","zixcbkgvbo","xkicvbogbz","vbkoicxgzb","vcbzgxbkoi","gicobbkvxz","xbzicbgovk","xobivgcbkz","kozgbibcvx","kviobzgcbx",
    "xibbzcogkv","ogzibxckbv","xbkgcbvioz","gokzivbbcx","bbcvkgxozi","bviczgxbko","kgzxocbibv","gbzvoxkcib","obvbxkcgzi","vgxcikzobb","xibcokgzvb","bkvgicozxb","kgvbbcioxz","obckibvgzx","ivkgbocbxz",
    "kgzcvibbxo","zvbcbkixog","obbvkxzicg","bvkbzgcoix","gbvicxzobk","kzbbvgcoxi","oxbcvzkgib","bzxboigcvk","xcokivbzgb","gkbozbcvxi","gvziockxbb","ivxbckgboz","vobbkzgxic","kxbcvbzgio","kxobbgicvz",
    "vxokgbbicz","gibkbvzoxc","cbivzgkbxo","ogizcxvbkb","icbzgxbkov","vobbckixgz","cbioxzkbgv","xvcbzoigkb","bobgkcxizv","obzkxgbcvi","cioxkbzbgv","ogvzbikcxb","zkxvobcigb","ogikcxvbzb","zivbbxkgco",
    "zixcbkgbvo","ikoxgzcbbv","xbgvbzikoc","xkobcgbviz","bvzibkocgx","vixbckgboz","covkbizxgb","gczvbbxiok","xbcvbgiozk","gvbxkbzcoi","vzbkcbixgo","bkivbzxogc","obbkxgzcvi","ixbozvcgkb","xbicokgzvb",
    "gczvobxibk","kbcvizgoxb","cizkbvogbx","oizvcbkbxg","gboxbcvzik","zkgoibcvxb",
    "cbbikxvzgo","kbvzobcgix","ocbzigxkbv","kicbgzxbov","ogizkxvbbc","kogvxcibbz","vbbxcgkzoi","ikzxbvgbco","xcizbgvbok","kxbzbvicgo","zbobkvxcig","ikgbvcoxzb","bkxcobvizg","xgivbbzock","boixkgzbcv",
    "coivbgkzxb","gkbibocxzv","cbbvgxkzio","bocxgbzikv","kogbzvbxic","czivxbbgko","ioxzbkgbcv","bckxobzgiv","xcgkivbzob","okcibzgbvx","vcbboxkzig","czbvxikgob","vzxcbokibg","kgbzbixcov","xbvgckbzio",
    "kigobxbczv","vxbczkgobi","bbvocigzxk","bxozgcibkv","xcgkvbiboz","oigbcxbkzv","vkxcgzbiob","kcziogxbvb","xkzbgivocb","boxcgbzikv","oibgxckbzv","bzcgxkbivo","kzboixgvbc","bkoixgvbcz","xzivbbgock",
    "vobbgzkxic","ozcvbxbigk","ickogvzbxb","xzbicbvgko","cozbxvbgik","izcobxbkvg","gokizvbxcb","ivocgzxkbb","kbcgbivoxz","kvxbczgboi","vkzoxbgibc","zbkgbcoxiv","gkoibvxbcz","vbizcxgbko","vbbxczoigk",
    "vbcgozbkxi","zxvgbbokci","cbbzvgkoix","kbczoivgbx","bkgiovbcxz","bvoczigbxk",
    "gcboxbvzik","zbvxgkobci","gkoxbbivcz","xcoigbvkbz","covgbizxkb","bboxgzvkic","bibvgxkzco","gkbobzxvci","obbvkcgzxi","zkgbcbixov","oixgbckvzb","vbzxbckigo","zogckxivbb","obvbzkixcg","cgibvxbokz",
    "kbczoigvbx","cgivzbkbxo","bxkzboivgc","gobzivbkcx","bkboicxvzg","coivkgbzxb","bgxvzcoibk","gbovzxcibk","kzoxcivbbg","bxovikgczb","kzgibovcxb","zboicgkxbv","kvoigczxbb","kxgbivbocz","gxbokczivb",
    "kigbcovxbz","zbgicokxbv","igobbzxckv","gxckivzbob","ixcokzbgvb","vbckixbgoz","gbvcxkibzo","ozckbxbigv","vgzkcioxbb","cbkbvioxzg","vxzbbckigo","obgxbivkcz","vxzoicbkgb","bigvxckzob","vbozicxkgb",
    "kgvboczibx","ziboxkgbcv","oicgzbkvbx","cokgxbbziv","bkixczgvbo","ikzxbvobcg","xkzbcigvob","xzkbcigvob","kgxbzibcvo","bkbozgvxci","kibzobcvxg","cvzgkxbobi","ocxkbbvzgi","bvbczgioxk","kbzicvbgox",
    "xobgvbcikz","oizgbxckbv","kbvgzxbcoi","kzbviogcxb","bocibxgvzk","ckzbvbogxi","bvoczigbkx","ckgbzbixvo","xzvkbgoibc","kigcxzbbov","obbzigvxkc","xibokcgvzb","xbgbokvzci","zbkobcxigv","ocbivzgxbk",
    "cbvkigbzox","zbgiockxbv","zgobxvcibk",
    "kbxizvbcgo","zxvkbogbci","bizvcbxokg","vxkzogibcb","ibogvzbckx","ivbkoxbzgc","bxgkcvbzoi","ivxbzkogcb","vbiogxczbk","kivxobgzbc","cikxozgbvb","zkcgbvbiox","gvoxzibkcb","xvzkibocgb","xvkoczgibb",
    "kvxzgoibbc","kgbczxboiv","xzckgvoibb","kbbviogcxz","ibozxkgcbv","gixobcvkzb","ckgibzoxbv","cxbibgvzok","zkcbovgxib","xgcibkbvzo","vikxbzogcb","bvokbcgizx","vbkgioxbcz","ibckbgvxzo","bgkxibzovc",
    "gcivbkbozx","xcgzkvoibb","ixcgzbbkvo","bozcbigkxv","bgzvxiokcb","okgbbxvizc","vkxiczgbob","bxbvikgczo","xgvizobbck","cibbkxogvz","bibgkoxczv","zcobvgxbki","zgvbkbcxio","vxbbckzigo","cigbxkozbv",
    "xvzgbcokib","kgiozbcxvb","ixcbgbzovk","bzvxogbcik","xiokczgbbv","zvicxobbgk","gcbvkzxboi","kvbixbgcoz","gbbvkxzico","cigoxbkvzb","vgozxkibbc","xbzgbiovck","bogvxzcbik","bvobgizcxk","vgozicxkbb",
    "bvckobzigx","ivbgkxcozb","xkzibvcogb","vgxkzcbbio","obgvcixzbk","zgbvokbxci","kczibgxovb","vbixzgbkoc","gicxbovkzb","vbbizcgkox","czbiogxvkb","ivzcgxobbk","bobzkcxigv","gbxkvoibzc","bgovikzxcb",
    "czbvxkigob","bbovigxczk","cbkbgioxzv","xickzgbobv","bcvozbgkxi","cvgxbozbki","zbocxvibgk","ixbcozbkvg","iczbbgkoxv","obgkcvbixz","ovgbbxkizc","bcgzvxbiok","zbkbvigoxc","ikbobxzgvc","bzivckobxg",
    "xoiczvgbkb","cbgibkxovz","ixkgbbzovc","izxgkbbvoc","xibbovzcgk","obgbzkxicv","kbbcizvxog","vbikgcxboz",
    "kcoigvbxbz","gocibbkvxz","vxokicbzbg","xcbgvkobzi","cibzobvgkx","bzivcbogxk","zvcbkobigx","ckbizoxbvg","zkibxbcgvo","xbigbvcokz"
]) == 926

assert sol.numSimilarGroups(["aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa",
"aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa","aaaaaaaaa"
]) == 1