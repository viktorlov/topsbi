from sqlalchemy.types import TEXT, SMALLINT, TIMESTAMP

Classes__dict = {
    'PK': SMALLINT,
    'Guid': TEXT,
    'GroupID': SMALLINT,
    'BaseClassID': SMALLINT,
    'Name': TEXT,
    'Comment': TEXT,
    'Icon': TEXT,
    'Sealed': SMALLINT,
    'Abstract': SMALLINT,
    'UseBaseClassIcon': SMALLINT,
    'Root': SMALLINT,
    'SystemType': SMALLINT,
    'PropertiesDisplayType': SMALLINT,
    'CreateFromPrototype': SMALLINT,
    'SupportsSaveAndCreate': SMALLINT,
    'UniqueIndexID': SMALLINT,
    'SchemeID': SMALLINT,
    'DefaultStageID': SMALLINT,
    'LinkedClassID': SMALLINT,
    'LinkedInheritClasses': SMALLINT,
    'Attributes': SMALLINT,
    'CanChange': SMALLINT,
    'InheritMasterClasses': SMALLINT,
    'Hidden': SMALLINT,
    'ObjectFormat': SMALLINT,
    'SupportMultiAttachment': SMALLINT
}

Classes__list = list(Classes__dict.keys())

plm__dict = {
    "s_PK": SMALLINT,
    "s_ObjectID": SMALLINT,
    "s_Guid": TEXT,
    "s_Version": SMALLINT,
    "s_ActualVersion": SMALLINT,
    "s_ClientViewID": SMALLINT,
    "s_Deleted": SMALLINT,
    "s_State": SMALLINT,
    "s_AuthorID": SMALLINT,
    "s_CreationDate": TIMESTAMP,
    "s_EditorID": SMALLINT,
    "s_EditDate": TIMESTAMP,
    "s_ClassID": SMALLINT,
    "s_AccessObjectID": SMALLINT,
    "s_SourceVersion": SMALLINT,
    "s_StageID": SMALLINT,
    "s_LinkedObjectID": SMALLINT,
    "s_LinkedObjectClassID": SMALLINT,
    "s_AccessLevel": SMALLINT,
    "s_OwnerID": SMALLINT,
    "s_LogicalObjectGuid": TEXT,
    "s_RevisionName": SMALLINT,
    "s_ActualRevision": SMALLINT,
    "oboznachenie_421975": TEXT,
    "Name": TEXT
}

plm__list = list(plm__dict.keys())

plmHierarchy__dict = {
    "s_PK": SMALLINT,
    "s_ObjectID": SMALLINT,
    "s_Guid": TEXT,
    "s_Version": SMALLINT,
    "s_ActualVersion": SMALLINT,
    "s_ClientViewID": SMALLINT,
    "s_Deleted": SMALLINT,
    "s_State": SMALLINT,
    "s_ParentID": SMALLINT,
    "s_FirstUse": SMALLINT,
    "s_HierarchyLinkID": SMALLINT
}

plmHierarchy__list = list(plmHierarchy__dict.keys())
