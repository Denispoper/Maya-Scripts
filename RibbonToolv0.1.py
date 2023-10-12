import maya.cmds as cmds


#------------------Inputs----------------------

targetDivisions = 10;
ribbonName = 'Leg_ribbon'

#----------------------------------------------

index = 0;

cmds.nurbsPlane( p=(0,0,0), ax=(0,0,1), lr=0.15, w=10, d=3, u=targetDivisions, v=1, ch=1, n=ribbonName )

cmds.select(ribbonName)

mel.eval('createHair ' + str(targetDivisions + 1) + ' 1 10 0 0 1 0 5 0 1 1 1;')

cmds.delete('pfxHair1')
cmds.delete('nucleus1')
cmds.delete('hairSystem1')

folliclesList = cmds.ls(ribbonName + 'Follicle*', typ="transform")

cmds.rename('hairSystem1Follicles', ribbonName + '_GRP')

print(folliclesList)

for follicle in folliclesList:
    toDeleteCurve = cmds.listRelatives(follicle, c=True, typ="transform")
    cmds.delete(toDeleteCurve)
    cmds.rename(follicle, ribbonName + '_follicle_' + str(index))   
    folliclesList[index] = ribbonName + '_follicle_' + str(index)
    jointName =  folliclesList[index] + '_joint'
    
    cmds.joint(n=jointName, rad=0.3)
    cmds.parent(jointName, folliclesList[index])
    cmds.setAttr(jointName + '.translate',0,0,0 )
    index += 1
    
