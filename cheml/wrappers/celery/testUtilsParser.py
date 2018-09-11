from cheml.wrappers.celery.utils import parse_graph
from collections import OrderedDict

# data = OrderedDict([('graph_id', 1),
#                     ('author', 'http://localhost:8000/api/users/1/'),
#                     ('created', '2018-06-01T14:31:19.659941Z'),
#                     ('title', 'init_template'),
#                     ('content', '{"elements":{"nodes":[{"data":{"id":"1a9ed18e-f384-472a-4e1a-277f22fc6dc4","name":"Enter : table","info":{"pandas":["read_excel","read_table"]},"params":{"wparams":[],"fparams":[{"type":"string","display_name":"convert_float","name":"convert_float","value":"","desc":"convert_float"},{"type":"string","display_name":"converters","name":"converters","value":"","desc":"converters"},{"type":"string","display_name":"date_parser","name":"date_parser","value":"","desc":"date_parser"},{"type":"string","display_name":"dtype","name":"dtype","value":"","desc":"dtype"},{"type":"string","display_name":"engine","name":"engine","value":"","desc":"engine"},{"type":"string","display_name":"false_values","name":"false_values","value":"","desc":"false_values"},{"type":"string","display_name":"header","name":"header","value":"","desc":"header"},{"type":"string","display_name":"index_col","name":"index_col","value":"","desc":"index_col"},{"type":"string","display_name":"io","name":"io","value":"","desc":"io"},{"type":"string","display_name":"na_values","name":"na_values","value":"","desc":"na_values"},{"type":"string","display_name":"names","name":"names","value":"","desc":"names"},{"type":"string","display_name":"parse_dates","name":"parse_dates","value":"","desc":"parse_dates"},{"type":"string","display_name":"sheet_name","name":"sheet_name","value":"","desc":"sheet_name"},{"type":"string","display_name":"skip_footer","name":"skip_footer","value":"","desc":"skip_footer"},{"type":"string","display_name":"skiprows","name":"skiprows","value":"","desc":"skiprows"},{"type":"string","display_name":"squeeze","name":"squeeze","value":"","desc":"squeeze"},{"type":"string","display_name":"thousands","name":"thousands","value":"","desc":"thousands"},{"type":"string","display_name":"true_values","name":"true_values","value":"","desc":"true_values"},{"type":"string","display_name":"usecols","name":"usecols","value":"","desc":"usecols"}]},"func":"read_excel","host":"pandas"},"position":{"x":146.4545454545455,"y":-60.66909068714485},"group":"nodes","removed":false,"selected":false,"selectable":true,"locked":false,"grabbable":true,"classes":""},{"data":{"id":"6822a0cb-6c80-1e6d-631b-1354a9f8f445","name":"Represent : molecular descriptors","info":{"cheml":["BagofBonds","CoulombMatrix","Dragon","RDKitFingerprint"]},"params":{"wparams":[],"fparams":[{"type":"string","display_name":"FPtype","name":"FPtype","value":"","desc":"FPtype"},{"type":"string","display_name":"arguments","name":"arguments","value":"","desc":"arguments"},{"type":"string","display_name":"molfile","name":"molfile","value":"","desc":"molfile"},{"type":"string","display_name":"nBits","name":"nBits","value":"","desc":"nBits"},{"type":"string","display_name":"path","name":"path","value":"","desc":"path"},{"type":"string","display_name":"radius","name":"radius","value":"","desc":"radius"},{"type":"string","display_name":"removeHs","name":"removeHs","value":"","desc":"removeHs"},{"type":"string","display_name":"vector","name":"vector","value":"","desc":"vector"}]},"func":"RDKitFingerprint","host":"cheml"},"position":{"x":170.98181818181814,"y":-2.232725715637173},"group":"nodes","removed":false,"selected":false,"selectable":true,"locked":false,"grabbable":true,"classes":""},{"data":{"id":"6d8f78e6-4a48-dd85-c128-9224d53433b6","name":"Prepare : data manipulation","info":{"cheml":["Split"],"pandas":["concat"]},"params":{"wparams":[],"fparams":[{"type":"string","display_name":"axis","name":"axis","value":"","desc":"axis"},{"type":"string","display_name":"copy","name":"copy","value":"","desc":"copy"},{"type":"string","display_name":"ignore_index","name":"ignore_index","value":"","desc":"ignore_index"},{"type":"string","display_name":"join","name":"join","value":"","desc":"join"},{"type":"string","display_name":"join_axes","name":"join_axes","value":"","desc":"join_axes"},{"type":"string","display_name":"keys","name":"keys","value":"","desc":"keys"},{"type":"string","display_name":"levels","name":"levels","value":"","desc":"levels"},{"type":"string","display_name":"names","name":"names","value":"","desc":"names"},{"type":"string","display_name":"verify_integrity","name":"verify_integrity","value":"","desc":"verify_integrity"}]},"func":"concat","host":"pandas"},"position":{"x":153.48181818181814,"y":59.26727428436283},"group":"nodes","removed":false,"selected":false,"selectable":true,"locked":false,"grabbable":true,"classes":""},{"data":{"id":"3be07cab-46fc-b01f-265f-27588188af55","name":"Model : regression","info":{"cheml":["MLP","MLP_sklearn"],"sklearn":["ARDRegression","BayesianRidge","ElasticNet","KernelRidge","Lars","Lasso","LassoLars","LinearRegression","LinearSVR","LogisticRegression","MLPRegressor","MultiTaskElasticNet","MultiTaskLasso","NuSVR","Ridge","SGDRegressor","SVR"]},"params":{"wparams":[{"type":"string","display_name":"func_method","name":"func_method","value":"","desc":"func_method"},{"type":"string","display_name":"track_header","name":"track_header","value":"","desc":"track_header"}],"fparams":[{"type":"string","display_name":"C","name":"C","value":"","desc":"C"},{"type":"string","display_name":"cache_size","name":"cache_size","value":"","desc":"cache_size"},{"type":"string","display_name":"coef0","name":"coef0","value":"","desc":"coef0"},{"type":"string","display_name":"degree","name":"degree","value":"","desc":"degree"},{"type":"string","display_name":"epsilon","name":"epsilon","value":"","desc":"epsilon"},{"type":"string","display_name":"gamma","name":"gamma","value":"","desc":"gamma"},{"type":"string","display_name":"kernel","name":"kernel","value":"","desc":"kernel"},{"type":"string","display_name":"max_iter","name":"max_iter","value":"","desc":"max_iter"},{"type":"string","display_name":"shrinking","name":"shrinking","value":"","desc":"shrinking"},{"type":"string","display_name":"tol","name":"tol","value":"","desc":"tol"},{"type":"string","display_name":"verbose","name":"verbose","value":"","desc":"verbose"}]},"func":"SVR","host":"sklearn"},"position":{"x":148.98181818181814,"y":132.26727428436283},"group":"nodes","removed":false,"selected":false,"selectable":true,"locked":false,"grabbable":true,"classes":""}],"edges":[{"data":{"source":"6822a0cb-6c80-1e6d-631b-1354a9f8f445","target":"6d8f78e6-4a48-dd85-c128-9224d53433b6","id":"690b7c86-81cc-49e4-916b-9ba66d1d3a4b","inputs":[{"type":"string","display_name":"df","name":"df","value":1,"desc":"df"},{"type":"string","display_name":"removed_rows","name":"removed_rows","value":"","desc":"removed_rows"}],"outputs":[{"type":"string","display_name":"df1","name":"df1","value":"","desc":"df1"},{"type":"string","display_name":"df2","name":"df2","value":1,"desc":"df2"},{"type":"string","display_name":"df3","name":"df3","value":"","desc":"df3"}]},"position":{},"group":"edges","removed":false,"selected":false,"selectable":true,"locked":false,"grabbable":true,"classes":""},{"data":{"source":"1a9ed18e-f384-472a-4e1a-277f22fc6dc4","target":"6822a0cb-6c80-1e6d-631b-1354a9f8f445","id":"c98d2601-850d-4b1f-87a9-06b5944d5114","inputs":[{"type":"string","display_name":"df","name":"df","value":1,"desc":"df"}],"outputs":[{"type":"string","display_name":"molfile","name":"molfile","value":1,"desc":"molfile"}]},"position":{},"group":"edges","removed":false,"selected":false,"selectable":true,"locked":false,"grabbable":true,"classes":""},{"data":{"source":"6d8f78e6-4a48-dd85-c128-9224d53433b6","target":"3be07cab-46fc-b01f-265f-27588188af55","id":"a1c7c983-cc16-4b73-a562-a3b52b77efc0","inputs":[{"type":"string","display_name":"df","name":"df","value":1,"desc":"df"}],"outputs":[{"type":"string","display_name":"api","name":"api","value":"","desc":"api"},{"type":"string","display_name":"dfx","name":"dfx","value":"","desc":"dfx"},{"type":"string","display_name":"dfy","name":"dfy","value":1,"desc":"dfy"}]},"position":{},"group":"edges","removed":false,"selected":false,"selectable":true,"locked":false,"grabbable":true,"classes":""}]},"style":[{"selector":"node","style":{"label":"data(name)","text-opacity":"0.5","text-valign":"center","text-halign":"right","background-color":"#11479e"}},{"selector":"edge","style":{"curve-style":"bezier","width":"4px","target-arrow-shape":"triangle","line-color":"#9dbaea","target-arrow-color":"#9dbaea"}},{"selector":".eh-handle","style":{"background-color":"red","width":"12px","height":"12px","shape":"ellipse","overlay-opacity":"0","border-width":"12px","border-opacity":"0"}},{"selector":".eh-hover","style":{"background-color":"red"}},{"selector":".eh-source","style":{"border-width":"2px","border-color":"red"}},{"selector":".eh-target","style":{"border-width":"2px","border-color":"red"}},{"selector":".eh-preview, .eh-ghost-edge","style":{"background-color":"red","line-color":"red","target-arrow-color":"red","source-arrow-color":"red"}}],"zoomingEnabled":true,"userZoomingEnabled":true,"zoom":0.7534075979678175,"minZoom":0.2,"maxZoom":2,"panningEnabled":true,"userPanningEnabled":true,"pan":{"x":164.02487223512134,"y":152.64575449253792},"boxSelectionEnabled":false,"renderer":{"name":"canvas"}}'),
#                     ('updated', '2018-06-20T18:22:02.485589Z')
#                     ])

data = OrderedDict([('graph_id', 12), ('author', 'http://localhost:8000/api/users/1/'), ('created', '2018-07-12T18:15:35.202719Z'), ('title', 'new12'), ('content', '{"elements":{"edges":[{"data":{"source":"6822a0cb-6c80-1e6d-631b-1354a9f8f445","target":"6d8f78e6-4a48-dd85-c128-9224d53433b6","id":"690b7c86-81cc-49e4-916b-9ba66d1d3a4b","inputs":[{"type":"string","display_name":"df","name":"df","value":"1","desc":"df"},{"type":"string","display_name":"removed_rows","name":"removed_rows","value":"2","desc":"removed_rows"}],"outputs":[{"type":"string","display_name":"df1","name":"df1","value":"1","desc":"df1"},{"type":"string","display_name":"df2","name":"df2","value":"","desc":"df2"},{"type":"string","display_name":"df3","name":"df3","value":"2","desc":"df3"}]},"position":{},"group":"edges","removed":false,"selected":false,"selectable":true,"locked":false,"grabbable":true,"classes":""},{"data":{"source":"1a9ed18e-f384-472a-4e1a-277f22fc6dc4","target":"6822a0cb-6c80-1e6d-631b-1354a9f8f445","id":"c98d2601-850d-4b1f-87a9-06b5944d5114","inputs":[{"type":"string","display_name":"df","name":"df","value":"1","desc":"df"}],"outputs":[{"type":"string","display_name":"molfile","name":"molfile","value":"1","desc":"molfile"}]},"position":{},"group":"edges","removed":false,"selected":false,"selectable":true,"locked":false,"grabbable":true,"classes":""},{"data":{"source":"6d8f78e6-4a48-dd85-c128-9224d53433b6","target":"3be07cab-46fc-b01f-265f-27588188af55","id":"a1c7c983-cc16-4b73-a562-a3b52b77efc0","inputs":[{"type":"string","display_name":"df","name":"df","value":"1","desc":"df"}],"outputs":[{"type":"string","display_name":"api","name":"api","value":"","desc":"api"},{"type":"string","display_name":"dfx","name":"dfx","value":"1","desc":"dfx"},{"type":"string","display_name":"dfy","name":"dfy","value":"1","desc":"dfy"}]},"position":{},"group":"edges","removed":false,"selected":false,"selectable":true,"locked":false,"grabbable":true,"classes":""}],"nodes":[{"data":{"id":"3be07cab-46fc-b01f-265f-27588188af55","name":"Model : regression","info":{"cheml":["MLP","MLP_sklearn"],"sklearn":["ARDRegression","BayesianRidge","ElasticNet","KernelRidge","Lars","Lasso","LassoLars","LinearRegression","LinearSVR","LogisticRegression","MLPRegressor","MultiTaskElasticNet","MultiTaskLasso","NuSVR","Ridge","SGDRegressor","SVR"]},"params":{"wparams":[{"type":"string","display_name":"func_method","name":"func_method","value":"","desc":"func_method"},{"type":"string","display_name":"track_header","name":"track_header","value":"","desc":"track_header"}],"fparams":[{"type":"string","display_name":"C","name":"C","value":"","desc":"C"},{"type":"string","display_name":"cache_size","name":"cache_size","value":"","desc":"cache_size"},{"type":"string","display_name":"coef0","name":"coef0","value":"","desc":"coef0"},{"type":"string","display_name":"degree","name":"degree","value":"","desc":"degree"},{"type":"string","display_name":"epsilon","name":"epsilon","value":"","desc":"epsilon"},{"type":"string","display_name":"gamma","name":"gamma","value":"","desc":"gamma"},{"type":"string","display_name":"kernel","name":"kernel","value":"","desc":"kernel"},{"type":"string","display_name":"max_iter","name":"max_iter","value":"","desc":"max_iter"},{"type":"string","display_name":"shrinking","name":"shrinking","value":"","desc":"shrinking"},{"type":"string","display_name":"tol","name":"tol","value":"","desc":"tol"},{"type":"string","display_name":"verbose","name":"verbose","value":"","desc":"verbose"}]},"func":"SVR","host":"sklearn"},"position":{"x":148.98181818181814,"y":132.26727428436283},"group":"nodes","removed":false,"selected":false,"selectable":true,"locked":false,"grabbable":true,"classes":""},{"data":{"id":"6d8f78e6-4a48-dd85-c128-9224d53433b6","name":"Prepare : data manipulation","info":{"cheml":["Split"],"pandas":["concat"]},"params":{"wparams":[],"fparams":[{"type":"string","display_name":"axis","name":"axis","value":"","desc":"axis"},{"type":"string","display_name":"copy","name":"copy","value":"","desc":"copy"},{"type":"string","display_name":"ignore_index","name":"ignore_index","value":"","desc":"ignore_index"},{"type":"string","display_name":"join","name":"join","value":"","desc":"join"},{"type":"string","display_name":"join_axes","name":"join_axes","value":"","desc":"join_axes"},{"type":"string","display_name":"keys","name":"keys","value":"","desc":"keys"},{"type":"string","display_name":"levels","name":"levels","value":"","desc":"levels"},{"type":"string","display_name":"names","name":"names","value":"","desc":"names"},{"type":"string","display_name":"verify_integrity","name":"verify_integrity","value":"","desc":"verify_integrity"}]},"func":"concat","host":"pandas"},"position":{"x":153.48181818181814,"y":59.26727428436283},"group":"nodes","removed":false,"selected":false,"selectable":true,"locked":false,"grabbable":true,"classes":""},{"data":{"id":"6822a0cb-6c80-1e6d-631b-1354a9f8f445","name":"Represent : molecular descriptors","info":{"cheml":["BagofBonds","CoulombMatrix","Dragon","RDKitFingerprint"]},"params":{"wparams":[],"fparams":[{"type":"string","display_name":"FPtype","name":"FPtype","value":"","desc":"FPtype"},{"type":"string","display_name":"arguments","name":"arguments","value":"","desc":"arguments"},{"type":"string","display_name":"molfile","name":"molfile","value":"","desc":"molfile"},{"type":"string","display_name":"nBits","name":"nBits","value":"","desc":"nBits"},{"type":"string","display_name":"path","name":"path","value":"","desc":"path"},{"type":"string","display_name":"radius","name":"radius","value":"","desc":"radius"},{"type":"string","display_name":"removeHs","name":"removeHs","value":"","desc":"removeHs"},{"type":"string","display_name":"vector","name":"vector","value":"","desc":"vector"}]},"func":"RDKitFingerprint","host":"cheml"},"position":{"x":170.98181818181814,"y":-2.232725715637173},"group":"nodes","removed":false,"selected":false,"selectable":true,"locked":false,"grabbable":true,"classes":""},{"data":{"id":"1a9ed18e-f384-472a-4e1a-277f22fc6dc4","name":"Enter : table","info":{"pandas":["read_excel","read_table"]},"params":{"wparams":[],"fparams":[{"type":"string","display_name":"convert_float","name":"convert_float","value":"","desc":"convert_float"},{"type":"string","display_name":"converters","name":"converters","value":"","desc":"converters"},{"type":"string","display_name":"date_parser","name":"date_parser","value":"","desc":"date_parser"},{"type":"string","display_name":"dtype","name":"dtype","value":"","desc":"dtype"},{"type":"string","display_name":"engine","name":"engine","value":"","desc":"engine"},{"type":"string","display_name":"false_values","name":"false_values","value":"","desc":"false_values"},{"type":"string","display_name":"header","name":"header","value":"","desc":"header"},{"type":"string","display_name":"index_col","name":"index_col","value":"","desc":"index_col"},{"type":"string","display_name":"io","name":"io","value":"","desc":"io"},{"type":"string","display_name":"na_values","name":"na_values","value":"","desc":"na_values"},{"type":"string","display_name":"names","name":"names","value":"","desc":"names"},{"type":"string","display_name":"parse_dates","name":"parse_dates","value":"","desc":"parse_dates"},{"type":"string","display_name":"sheet_name","name":"sheet_name","value":"","desc":"sheet_name"},{"type":"string","display_name":"skip_footer","name":"skip_footer","value":"","desc":"skip_footer"},{"type":"string","display_name":"skiprows","name":"skiprows","value":"","desc":"skiprows"},{"type":"string","display_name":"squeeze","name":"squeeze","value":"","desc":"squeeze"},{"type":"string","display_name":"thousands","name":"thousands","value":"","desc":"thousands"},{"type":"string","display_name":"true_values","name":"true_values","value":"","desc":"true_values"},{"type":"string","display_name":"usecols","name":"usecols","value":"","desc":"usecols"}]},"func":"read_excel","host":"pandas"},"position":{"x":146.4545454545455,"y":-60.66909068714485},"group":"nodes","removed":false,"selected":false,"selectable":true,"locked":false,"grabbable":true,"classes":""},{"data":{"id":"e04b847a-c948-47b2-9748-1449ddc0ac8b"},"position":{"x":148.98181818181814,"y":117.26727428436283},"group":"nodes","removed":false,"selected":false,"selectable":false,"locked":false,"grabbable":false,"classes":"eh-handle"}]},"style":[{"selector":"node","style":{"label":"data(name)","text-opacity":"0.5","text-valign":"center","text-halign":"right","background-color":"#11479e"}},{"selector":"edge","style":{"curve-style":"bezier","width":"4px","target-arrow-shape":"triangle","line-color":"#9dbaea","target-arrow-color":"#9dbaea"}},{"selector":".eh-handle","style":{"background-color":"red","width":"12px","height":"12px","shape":"ellipse","overlay-opacity":"0","border-width":"12px","border-opacity":"0"}},{"selector":".eh-hover","style":{"background-color":"red"}},{"selector":".eh-source","style":{"border-width":"2px","border-color":"red"}},{"selector":".eh-target","style":{"border-width":"2px","border-color":"red"}},{"selector":".eh-preview, .eh-ghost-edge","style":{"background-color":"red","line-color":"red","target-arrow-color":"red","source-arrow-color":"red"}}],"zoomingEnabled":true,"userZoomingEnabled":true,"zoom":2,"minZoom":0.2,"maxZoom":2,"panningEnabled":true,"userPanningEnabled":true,"pan":{"x":-69.45668484516415,"y":50.77018972862146},"boxSelectionEnabled":false,"renderer":{"name":"canvas"}}'), ('updated', '2018-07-12T18:15:35.206888Z')])


cmls, dep_lists, comp_graph = parse_graph(data)

for node in cmls:
    print(node)

print(dep_lists)

print(comp_graph)
