# Clear Case commands

```
cleartool serview <owername>

cleartool lsview |grep <owername>

cleartool catcs
cleartool setcs <owername>

cleartool rmview -f -tag <owername>

cleartool edcs

cleartool lsco -r -me
cleartool lsco -r |grep <owername>

cleartool pwv

cleartool lsprivate | grep -v checkedout | xargs rm -rf

cleartool mkview -stgloc ims_1views -tag mgc5.2_dim_econzho

cleartool co -unr -nc filename
cleartool ci -nc filename

cleartool unco filename

makepack
```
