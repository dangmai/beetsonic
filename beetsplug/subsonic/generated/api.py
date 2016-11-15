# .\beetsplug\subsonic\generated\api.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:dc8ebe00992167d927839951885240a59c8d17f2
# Generated 2016-11-15 17:55:00.628000 by PyXB version 1.2.5 using Python 2.7.8.final.0
# Namespace http://subsonic.org/restapi

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:8989b6d1-ab86-11e6-878a-cc3d829ae560')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.5'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://subsonic.org/restapi', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: {http://subsonic.org/restapi}ResponseStatus
class ResponseStatus (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ResponseStatus')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 60, 4)
    _Documentation = None
ResponseStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ResponseStatus, enum_prefix=None)
ResponseStatus.ok = ResponseStatus._CF_enumeration.addEnumeration(unicode_value='ok', tag='ok')
ResponseStatus.failed = ResponseStatus._CF_enumeration.addEnumeration(unicode_value='failed', tag='failed')
ResponseStatus._InitializeFacetMap(ResponseStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ResponseStatus', ResponseStatus)
_module_typeBindings.ResponseStatus = ResponseStatus

# Atomic simple type: {http://subsonic.org/restapi}Version
class Version (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Version')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 67, 4)
    _Documentation = None
Version._CF_pattern = pyxb.binding.facets.CF_pattern()
Version._CF_pattern.addPattern(pattern='\\d+\\.\\d+\\.\\d+')
Version._InitializeFacetMap(Version._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'Version', Version)
_module_typeBindings.Version = Version

# Atomic simple type: {http://subsonic.org/restapi}MediaType
class MediaType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MediaType')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 256, 4)
    _Documentation = None
MediaType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MediaType, enum_prefix=None)
MediaType.music = MediaType._CF_enumeration.addEnumeration(unicode_value='music', tag='music')
MediaType.podcast = MediaType._CF_enumeration.addEnumeration(unicode_value='podcast', tag='podcast')
MediaType.audiobook = MediaType._CF_enumeration.addEnumeration(unicode_value='audiobook', tag='audiobook')
MediaType.video = MediaType._CF_enumeration.addEnumeration(unicode_value='video', tag='video')
MediaType._InitializeFacetMap(MediaType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MediaType', MediaType)
_module_typeBindings.MediaType = MediaType

# Atomic simple type: {http://subsonic.org/restapi}UserRating
class UserRating (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UserRating')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 265, 4)
    _Documentation = None
UserRating._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=UserRating, value=pyxb.binding.datatypes.int(1))
UserRating._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=UserRating, value=pyxb.binding.datatypes.int(5))
UserRating._InitializeFacetMap(UserRating._CF_minInclusive,
   UserRating._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'UserRating', UserRating)
_module_typeBindings.UserRating = UserRating

# Atomic simple type: {http://subsonic.org/restapi}AverageRating
class AverageRating (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AverageRating')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 272, 4)
    _Documentation = None
AverageRating._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=AverageRating, value=pyxb.binding.datatypes.double(1.0))
AverageRating._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=AverageRating, value=pyxb.binding.datatypes.double(5.0))
AverageRating._InitializeFacetMap(AverageRating._CF_minInclusive,
   AverageRating._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'AverageRating', AverageRating)
_module_typeBindings.AverageRating = AverageRating

# Atomic simple type: {http://subsonic.org/restapi}PodcastStatus
class PodcastStatus (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PodcastStatus')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 443, 4)
    _Documentation = None
PodcastStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PodcastStatus, enum_prefix=None)
PodcastStatus.new = PodcastStatus._CF_enumeration.addEnumeration(unicode_value='new', tag='new')
PodcastStatus.downloading = PodcastStatus._CF_enumeration.addEnumeration(unicode_value='downloading', tag='downloading')
PodcastStatus.completed = PodcastStatus._CF_enumeration.addEnumeration(unicode_value='completed', tag='completed')
PodcastStatus.error = PodcastStatus._CF_enumeration.addEnumeration(unicode_value='error', tag='error')
PodcastStatus.deleted = PodcastStatus._CF_enumeration.addEnumeration(unicode_value='deleted', tag='deleted')
PodcastStatus.skipped = PodcastStatus._CF_enumeration.addEnumeration(unicode_value='skipped', tag='skipped')
PodcastStatus._InitializeFacetMap(PodcastStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'PodcastStatus', PodcastStatus)
_module_typeBindings.PodcastStatus = PodcastStatus

# Complex type {http://subsonic.org/restapi}MusicFolders with content type ELEMENT_ONLY
class MusicFolders (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://subsonic.org/restapi}MusicFolders with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MusicFolders')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 73, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://subsonic.org/restapi}musicFolder uses Python identifier musicFolder
    __musicFolder = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'musicFolder'), 'musicFolder', '__httpsubsonic_orgrestapi_MusicFolders_httpsubsonic_orgrestapimusicFolder', True, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 75, 12), )

    
    musicFolder = property(__musicFolder.value, __musicFolder.set, None, None)

    _ElementMap.update({
        __musicFolder.name() : __musicFolder
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.MusicFolders = MusicFolders
Namespace.addCategoryObject('typeBinding', 'MusicFolders', MusicFolders)


# Complex type {http://subsonic.org/restapi}MusicFolder with content type EMPTY
class MusicFolder (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://subsonic.org/restapi}MusicFolder with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MusicFolder')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 79, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpsubsonic_orgrestapi_MusicFolder_id', pyxb.binding.datatypes.int, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 80, 8)
    __id._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 80, 8)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpsubsonic_orgrestapi_MusicFolder_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 81, 8)
    __name._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 81, 8)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __name.name() : __name
    })
_module_typeBindings.MusicFolder = MusicFolder
Namespace.addCategoryObject('typeBinding', 'MusicFolder', MusicFolder)


# Complex type {http://subsonic.org/restapi}Indexes with content type ELEMENT_ONLY
class Indexes (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://subsonic.org/restapi}Indexes with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Indexes')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 84, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://subsonic.org/restapi}shortcut uses Python identifier shortcut
    __shortcut = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'shortcut'), 'shortcut', '__httpsubsonic_orgrestapi_Indexes_httpsubsonic_orgrestapishortcut', True, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 86, 12), )

    
    shortcut = property(__shortcut.value, __shortcut.set, None, None)

    
    # Element {http://subsonic.org/restapi}index uses Python identifier index
    __index = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'index'), 'index', '__httpsubsonic_orgrestapi_Indexes_httpsubsonic_orgrestapiindex', True, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 87, 12), )

    
    index = property(__index.value, __index.set, None, None)

    
    # Element {http://subsonic.org/restapi}child uses Python identifier child
    __child = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'child'), 'child', '__httpsubsonic_orgrestapi_Indexes_httpsubsonic_orgrestapichild', True, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 88, 12), )

    
    child = property(__child.value, __child.set, None, None)

    
    # Attribute lastModified uses Python identifier lastModified
    __lastModified = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lastModified'), 'lastModified', '__httpsubsonic_orgrestapi_Indexes_lastModified', pyxb.binding.datatypes.long, required=True)
    __lastModified._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 90, 8)
    __lastModified._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 90, 8)
    
    lastModified = property(__lastModified.value, __lastModified.set, None, None)

    
    # Attribute ignoredArticles uses Python identifier ignoredArticles
    __ignoredArticles = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ignoredArticles'), 'ignoredArticles', '__httpsubsonic_orgrestapi_Indexes_ignoredArticles', pyxb.binding.datatypes.string, required=True)
    __ignoredArticles._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 91, 8)
    __ignoredArticles._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 91, 8)
    
    ignoredArticles = property(__ignoredArticles.value, __ignoredArticles.set, None, None)

    _ElementMap.update({
        __shortcut.name() : __shortcut,
        __index.name() : __index,
        __child.name() : __child
    })
    _AttributeMap.update({
        __lastModified.name() : __lastModified,
        __ignoredArticles.name() : __ignoredArticles
    })
_module_typeBindings.Indexes = Indexes
Namespace.addCategoryObject('typeBinding', 'Indexes', Indexes)


# Complex type {http://subsonic.org/restapi}Index with content type ELEMENT_ONLY
class Index (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://subsonic.org/restapi}Index with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Index')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 94, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://subsonic.org/restapi}artist uses Python identifier artist
    __artist = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'artist'), 'artist', '__httpsubsonic_orgrestapi_Index_httpsubsonic_orgrestapiartist', True, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 96, 12), )

    
    artist = property(__artist.value, __artist.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpsubsonic_orgrestapi_Index_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 98, 8)
    __name._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 98, 8)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        __artist.name() : __artist
    })
    _AttributeMap.update({
        __name.name() : __name
    })
_module_typeBindings.Index = Index
Namespace.addCategoryObject('typeBinding', 'Index', Index)


# Complex type {http://subsonic.org/restapi}Genres with content type ELEMENT_ONLY
class Genres (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://subsonic.org/restapi}Genres with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Genres')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 109, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://subsonic.org/restapi}genre uses Python identifier genre
    __genre = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'genre'), 'genre', '__httpsubsonic_orgrestapi_Genres_httpsubsonic_orgrestapigenre', True, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 111, 12), )

    
    genre = property(__genre.value, __genre.set, None, None)

    _ElementMap.update({
        __genre.name() : __genre
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Genres = Genres
Namespace.addCategoryObject('typeBinding', 'Genres', Genres)


# Complex type {http://subsonic.org/restapi}Genre with content type MIXED
class Genre (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://subsonic.org/restapi}Genre with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Genre')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 115, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute songCount uses Python identifier songCount
    __songCount = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'songCount'), 'songCount', '__httpsubsonic_orgrestapi_Genre_songCount', pyxb.binding.datatypes.int, required=True)
    __songCount._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 116, 8)
    __songCount._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 116, 8)
    
    songCount = property(__songCount.value, __songCount.set, None, None)

    
    # Attribute albumCount uses Python identifier albumCount
    __albumCount = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'albumCount'), 'albumCount', '__httpsubsonic_orgrestapi_Genre_albumCount', pyxb.binding.datatypes.int, required=True)
    __albumCount._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 117, 8)
    __albumCount._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 117, 8)
    
    albumCount = property(__albumCount.value, __albumCount.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __songCount.name() : __songCount,
        __albumCount.name() : __albumCount
    })
_module_typeBindings.Genre = Genre
Namespace.addCategoryObject('typeBinding', 'Genre', Genre)


# Complex type {http://subsonic.org/restapi}ArtistsID3 with content type ELEMENT_ONLY
class ArtistsID3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://subsonic.org/restapi}ArtistsID3 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ArtistsID3')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 120, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://subsonic.org/restapi}index uses Python identifier index
    __index = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'index'), 'index', '__httpsubsonic_orgrestapi_ArtistsID3_httpsubsonic_orgrestapiindex', True, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 122, 12), )

    
    index = property(__index.value, __index.set, None, None)

    
    # Attribute ignoredArticles uses Python identifier ignoredArticles
    __ignoredArticles = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ignoredArticles'), 'ignoredArticles', '__httpsubsonic_orgrestapi_ArtistsID3_ignoredArticles', pyxb.binding.datatypes.string, required=True)
    __ignoredArticles._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 124, 8)
    __ignoredArticles._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 124, 8)
    
    ignoredArticles = property(__ignoredArticles.value, __ignoredArticles.set, None, None)

    _ElementMap.update({
        __index.name() : __index
    })
    _AttributeMap.update({
        __ignoredArticles.name() : __ignoredArticles
    })
_module_typeBindings.ArtistsID3 = ArtistsID3
Namespace.addCategoryObject('typeBinding', 'ArtistsID3', ArtistsID3)


# Complex type {http://subsonic.org/restapi}IndexID3 with content type ELEMENT_ONLY
class IndexID3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://subsonic.org/restapi}IndexID3 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IndexID3')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 127, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://subsonic.org/restapi}artist uses Python identifier artist
    __artist = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'artist'), 'artist', '__httpsubsonic_orgrestapi_IndexID3_httpsubsonic_orgrestapiartist', True, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 129, 12), )

    
    artist = property(__artist.value, __artist.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpsubsonic_orgrestapi_IndexID3_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 131, 8)
    __name._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 131, 8)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        __artist.name() : __artist
    })
    _AttributeMap.update({
        __name.name() : __name
    })
_module_typeBindings.IndexID3 = IndexID3
Namespace.addCategoryObject('typeBinding', 'IndexID3', IndexID3)


# Complex type {http://subsonic.org/restapi}ArtistID3 with content type EMPTY
class ArtistID3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://subsonic.org/restapi}ArtistID3 with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ArtistID3')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 134, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpsubsonic_orgrestapi_ArtistID3_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 135, 8)
    __id._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 135, 8)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpsubsonic_orgrestapi_ArtistID3_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 136, 8)
    __name._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 136, 8)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute coverArt uses Python identifier coverArt
    __coverArt = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'coverArt'), 'coverArt', '__httpsubsonic_orgrestapi_ArtistID3_coverArt', pyxb.binding.datatypes.string)
    __coverArt._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 137, 8)
    __coverArt._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 137, 8)
    
    coverArt = property(__coverArt.value, __coverArt.set, None, None)

    
    # Attribute albumCount uses Python identifier albumCount
    __albumCount = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'albumCount'), 'albumCount', '__httpsubsonic_orgrestapi_ArtistID3_albumCount', pyxb.binding.datatypes.int, required=True)
    __albumCount._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 138, 8)
    __albumCount._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 138, 8)
    
    albumCount = property(__albumCount.value, __albumCount.set, None, None)

    
    # Attribute starred uses Python identifier starred
    __starred = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'starred'), 'starred', '__httpsubsonic_orgrestapi_ArtistID3_starred', pyxb.binding.datatypes.dateTime)
    __starred._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 139, 8)
    __starred._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 139, 8)
    
    starred = property(__starred.value, __starred.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __name.name() : __name,
        __coverArt.name() : __coverArt,
        __albumCount.name() : __albumCount,
        __starred.name() : __starred
    })
_module_typeBindings.ArtistID3 = ArtistID3
Namespace.addCategoryObject('typeBinding', 'ArtistID3', ArtistID3)


# Complex type {http://subsonic.org/restapi}AlbumID3 with content type EMPTY
class AlbumID3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://subsonic.org/restapi}AlbumID3 with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AlbumID3')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 152, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpsubsonic_orgrestapi_AlbumID3_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 153, 8)
    __id._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 153, 8)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpsubsonic_orgrestapi_AlbumID3_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 154, 8)
    __name._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 154, 8)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute artist uses Python identifier artist
    __artist = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'artist'), 'artist', '__httpsubsonic_orgrestapi_AlbumID3_artist', pyxb.binding.datatypes.string)
    __artist._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 155, 8)
    __artist._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 155, 8)
    
    artist = property(__artist.value, __artist.set, None, None)

    
    # Attribute artistId uses Python identifier artistId
    __artistId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'artistId'), 'artistId', '__httpsubsonic_orgrestapi_AlbumID3_artistId', pyxb.binding.datatypes.string)
    __artistId._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 156, 8)
    __artistId._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 156, 8)
    
    artistId = property(__artistId.value, __artistId.set, None, None)

    
    # Attribute coverArt uses Python identifier coverArt
    __coverArt = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'coverArt'), 'coverArt', '__httpsubsonic_orgrestapi_AlbumID3_coverArt', pyxb.binding.datatypes.string)
    __coverArt._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 157, 8)
    __coverArt._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 157, 8)
    
    coverArt = property(__coverArt.value, __coverArt.set, None, None)

    
    # Attribute songCount uses Python identifier songCount
    __songCount = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'songCount'), 'songCount', '__httpsubsonic_orgrestapi_AlbumID3_songCount', pyxb.binding.datatypes.int, required=True)
    __songCount._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 158, 8)
    __songCount._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 158, 8)
    
    songCount = property(__songCount.value, __songCount.set, None, None)

    
    # Attribute duration uses Python identifier duration
    __duration = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'duration'), 'duration', '__httpsubsonic_orgrestapi_AlbumID3_duration', pyxb.binding.datatypes.int, required=True)
    __duration._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 159, 8)
    __duration._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 159, 8)
    
    duration = property(__duration.value, __duration.set, None, None)

    
    # Attribute playCount uses Python identifier playCount
    __playCount = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'playCount'), 'playCount', '__httpsubsonic_orgrestapi_AlbumID3_playCount', pyxb.binding.datatypes.long)
    __playCount._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 160, 8)
    __playCount._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 160, 8)
    
    playCount = property(__playCount.value, __playCount.set, None, None)

    
    # Attribute created uses Python identifier created
    __created = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'created'), 'created', '__httpsubsonic_orgrestapi_AlbumID3_created', pyxb.binding.datatypes.dateTime, required=True)
    __created._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 161, 8)
    __created._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 161, 8)
    
    created = property(__created.value, __created.set, None, None)

    
    # Attribute starred uses Python identifier starred
    __starred = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'starred'), 'starred', '__httpsubsonic_orgrestapi_AlbumID3_starred', pyxb.binding.datatypes.dateTime)
    __starred._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 162, 8)
    __starred._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 162, 8)
    
    starred = property(__starred.value, __starred.set, None, None)

    
    # Attribute year uses Python identifier year
    __year = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'year'), 'year', '__httpsubsonic_orgrestapi_AlbumID3_year', pyxb.binding.datatypes.int)
    __year._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 163, 8)
    __year._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 163, 8)
    
    year = property(__year.value, __year.set, None, None)

    
    # Attribute genre uses Python identifier genre
    __genre = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'genre'), 'genre', '__httpsubsonic_orgrestapi_AlbumID3_genre', pyxb.binding.datatypes.string)
    __genre._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 164, 8)
    __genre._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 164, 8)
    
    genre = property(__genre.value, __genre.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __name.name() : __name,
        __artist.name() : __artist,
        __artistId.name() : __artistId,
        __coverArt.name() : __coverArt,
        __songCount.name() : __songCount,
        __duration.name() : __duration,
        __playCount.name() : __playCount,
        __created.name() : __created,
        __starred.name() : __starred,
        __year.name() : __year,
        __genre.name() : __genre
    })
_module_typeBindings.AlbumID3 = AlbumID3
Namespace.addCategoryObject('typeBinding', 'AlbumID3', AlbumID3)


# Complex type {http://subsonic.org/restapi}Videos with content type ELEMENT_ONLY
class Videos (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://subsonic.org/restapi}Videos with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Videos')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 177, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://subsonic.org/restapi}video uses Python identifier video
    __video = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'video'), 'video', '__httpsubsonic_orgrestapi_Videos_httpsubsonic_orgrestapivideo', True, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 179, 12), )

    
    video = property(__video.value, __video.set, None, None)

    _ElementMap.update({
        __video.name() : __video
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Videos = Videos
Namespace.addCategoryObject('typeBinding', 'Videos', Videos)


# Complex type {http://subsonic.org/restapi}VideoInfo with content type ELEMENT_ONLY
class VideoInfo (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://subsonic.org/restapi}VideoInfo with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VideoInfo')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 183, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://subsonic.org/restapi}captions uses Python identifier captions
    __captions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'captions'), 'captions', '__httpsubsonic_orgrestapi_VideoInfo_httpsubsonic_orgrestapicaptions', True, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 185, 12), )

    
    captions = property(__captions.value, __captions.set, None, None)

    
    # Element {http://subsonic.org/restapi}audioTrack uses Python identifier audioTrack
    __audioTrack = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'audioTrack'), 'audioTrack', '__httpsubsonic_orgrestapi_VideoInfo_httpsubsonic_orgrestapiaudioTrack', True, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 186, 12), )

    
    audioTrack = property(__audioTrack.value, __audioTrack.set, None, None)

    
    # Element {http://subsonic.org/restapi}conversion uses Python identifier conversion
    __conversion = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'conversion'), 'conversion', '__httpsubsonic_orgrestapi_VideoInfo_httpsubsonic_orgrestapiconversion', True, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 187, 12), )

    
    conversion = property(__conversion.value, __conversion.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpsubsonic_orgrestapi_VideoInfo_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 189, 8)
    __id._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 189, 8)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __captions.name() : __captions,
        __audioTrack.name() : __audioTrack,
        __conversion.name() : __conversion
    })
    _AttributeMap.update({
        __id.name() : __id
    })
_module_typeBindings.VideoInfo = VideoInfo
Namespace.addCategoryObject('typeBinding', 'VideoInfo', VideoInfo)


# Complex type {http://subsonic.org/restapi}Captions with content type EMPTY
class Captions (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://subsonic.org/restapi}Captions with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Captions')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 192, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpsubsonic_orgrestapi_Captions_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 193, 8)
    __id._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 193, 8)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpsubsonic_orgrestapi_Captions_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 194, 8)
    __name._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 194, 8)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __name.name() : __name
    })
_module_typeBindings.Captions = Captions
Namespace.addCategoryObject('typeBinding', 'Captions', Captions)


# Complex type {http://subsonic.org/restapi}AudioTrack with content type EMPTY
class AudioTrack (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://subsonic.org/restapi}AudioTrack with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AudioTrack')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 197, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpsubsonic_orgrestapi_AudioTrack_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 198, 8)
    __id._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 198, 8)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpsubsonic_orgrestapi_AudioTrack_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 199, 8)
    __name._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 199, 8)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute languageCode uses Python identifier languageCode
    __languageCode = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'languageCode'), 'languageCode', '__httpsubsonic_orgrestapi_AudioTrack_languageCode', pyxb.binding.datatypes.string)
    __languageCode._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 200, 8)
    __languageCode._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 200, 8)
    
    languageCode = property(__languageCode.value, __languageCode.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __name.name() : __name,
        __languageCode.name() : __languageCode
    })
_module_typeBindings.AudioTrack = AudioTrack
Namespace.addCategoryObject('typeBinding', 'AudioTrack', AudioTrack)


# Complex type {http://subsonic.org/restapi}VideoConversion with content type EMPTY
class VideoConversion (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://subsonic.org/restapi}VideoConversion with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VideoConversion')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 203, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpsubsonic_orgrestapi_VideoConversion_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 204, 8)
    __id._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 204, 8)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute bitRate uses Python identifier bitRate
    __bitRate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'bitRate'), 'bitRate', '__httpsubsonic_orgrestapi_VideoConversion_bitRate', pyxb.binding.datatypes.int)
    __bitRate._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 205, 8)
    __bitRate._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 205, 8)
    
    bitRate = property(__bitRate.value, __bitRate.set, None, None)

    
    # Attribute audioTrackId uses Python identifier audioTrackId
    __audioTrackId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'audioTrackId'), 'audioTrackId', '__httpsubsonic_orgrestapi_VideoConversion_audioTrackId', pyxb.binding.datatypes.int)
    __audioTrackId._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 206, 8)
    __audioTrackId._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 206, 8)
    
    audioTrackId = property(__audioTrackId.value, __audioTrackId.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __bitRate.name() : __bitRate,
        __audioTrackId.name() : __audioTrackId
    })
_module_typeBindings.VideoConversion = VideoConversion
Namespace.addCategoryObject('typeBinding', 'VideoConversion', VideoConversion)


# Complex type {http://subsonic.org/restapi}NowPlaying with content type ELEMENT_ONLY
class NowPlaying (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://subsonic.org/restapi}NowPlaying with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NowPlaying')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 279, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://subsonic.org/restapi}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'entry'), 'entry', '__httpsubsonic_orgrestapi_NowPlaying_httpsubsonic_orgrestapientry', True, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 281, 12), )

    
    entry = property(__entry.value, __entry.set, None, None)

    _ElementMap.update({
        __entry.name() : __entry
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.NowPlaying = NowPlaying
Namespace.addCategoryObject('typeBinding', 'NowPlaying', NowPlaying)


# Complex type {http://subsonic.org/restapi}SearchResult with content type ELEMENT_ONLY
class SearchResult (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://subsonic.org/restapi}SearchResult with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SearchResult')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 297, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://subsonic.org/restapi}match uses Python identifier match
    __match = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'match'), 'match', '__httpsubsonic_orgrestapi_SearchResult_httpsubsonic_orgrestapimatch', True, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 299, 12), )

    
    match = property(__match.value, __match.set, None, None)

    
    # Attribute offset uses Python identifier offset
    __offset = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'offset'), 'offset', '__httpsubsonic_orgrestapi_SearchResult_offset', pyxb.binding.datatypes.int, required=True)
    __offset._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 301, 8)
    __offset._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 301, 8)
    
    offset = property(__offset.value, __offset.set, None, None)

    
    # Attribute totalHits uses Python identifier totalHits
    __totalHits = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'totalHits'), 'totalHits', '__httpsubsonic_orgrestapi_SearchResult_totalHits', pyxb.binding.datatypes.int, required=True)
    __totalHits._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 302, 8)
    __totalHits._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 302, 8)
    
    totalHits = property(__totalHits.value, __totalHits.set, None, None)

    _ElementMap.update({
        __match.name() : __match
    })
    _AttributeMap.update({
        __offset.name() : __offset,
        __totalHits.name() : __totalHits
    })
_module_typeBindings.SearchResult = SearchResult
Namespace.addCategoryObject('typeBinding', 'SearchResult', SearchResult)


# Complex type {http://subsonic.org/restapi}SearchResult2 with content type ELEMENT_ONLY
class SearchResult2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://subsonic.org/restapi}SearchResult2 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SearchResult2')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 305, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://subsonic.org/restapi}artist uses Python identifier artist
    __artist = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'artist'), 'artist', '__httpsubsonic_orgrestapi_SearchResult2_httpsubsonic_orgrestapiartist', True, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 307, 12), )

    
    artist = property(__artist.value, __artist.set, None, None)

    
    # Element {http://subsonic.org/restapi}album uses Python identifier album
    __album = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'album'), 'album', '__httpsubsonic_orgrestapi_SearchResult2_httpsubsonic_orgrestapialbum', True, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 308, 12), )

    
    album = property(__album.value, __album.set, None, None)

    
    # Element {http://subsonic.org/restapi}song uses Python identifier song
    __song = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'song'), 'song', '__httpsubsonic_orgrestapi_SearchResult2_httpsubsonic_orgrestapisong', True, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 309, 12), )

    
    song = property(__song.value, __song.set, None, None)

    _ElementMap.update({
        __artist.name() : __artist,
        __album.name() : __album,
        __song.name() : __song
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SearchResult2 = SearchResult2
Namespace.addCategoryObject('typeBinding', 'SearchResult2', SearchResult2)


# Complex type {http://subsonic.org/restapi}SearchResult3 with content type ELEMENT_ONLY
class SearchResult3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://subsonic.org/restapi}SearchResult3 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SearchResult3')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 313, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://subsonic.org/restapi}artist uses Python identifier artist
    __artist = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'artist'), 'artist', '__httpsubsonic_orgrestapi_SearchResult3_httpsubsonic_orgrestapiartist', True, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 315, 12), )

    
    artist = property(__artist.value, __artist.set, None, None)

    
    # Element {http://subsonic.org/restapi}album uses Python identifier album
    __album = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'album'), 'album', '__httpsubsonic_orgrestapi_SearchResult3_httpsubsonic_orgrestapialbum', True, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 316, 12), )

    
    album = property(__album.value, __album.set, None, None)

    
    # Element {http://subsonic.org/restapi}song uses Python identifier song
    __song = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'song'), 'song', '__httpsubsonic_orgrestapi_SearchResult3_httpsubsonic_orgrestapisong', True, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 317, 12), )

    
    song = property(__song.value, __song.set, None, None)

    _ElementMap.update({
        __artist.name() : __artist,
        __album.name() : __album,
        __song.name() : __song
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SearchResult3 = SearchResult3
Namespace.addCategoryObject('typeBinding', 'SearchResult3', SearchResult3)


# Complex type {http://subsonic.org/restapi}Playlists with content type ELEMENT_ONLY
class Playlists (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://subsonic.org/restapi}Playlists with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Playlists')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 321, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://subsonic.org/restapi}playlist uses Python identifier playlist
    __playlist = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'playlist'), 'playlist', '__httpsubsonic_orgrestapi_Playlists_httpsubsonic_orgrestapiplaylist', True, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 323, 12), )

    
    playlist = property(__playlist.value, __playlist.set, None, None)

    _ElementMap.update({
        __playlist.name() : __playlist
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Playlists = Playlists
Namespace.addCategoryObject('typeBinding', 'Playlists', Playlists)


# Complex type {http://subsonic.org/restapi}Playlist with content type ELEMENT_ONLY
class Playlist (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://subsonic.org/restapi}Playlist with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Playlist')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 327, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://subsonic.org/restapi}allowedUser uses Python identifier allowedUser
    __allowedUser = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'allowedUser'), 'allowedUser', '__httpsubsonic_orgrestapi_Playlist_httpsubsonic_orgrestapiallowedUser', True, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 329, 12), )

    
    allowedUser = property(__allowedUser.value, __allowedUser.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpsubsonic_orgrestapi_Playlist_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 331, 8)
    __id._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 331, 8)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpsubsonic_orgrestapi_Playlist_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 332, 8)
    __name._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 332, 8)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute comment uses Python identifier comment
    __comment = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'comment'), 'comment', '__httpsubsonic_orgrestapi_Playlist_comment', pyxb.binding.datatypes.string)
    __comment._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 333, 8)
    __comment._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 333, 8)
    
    comment = property(__comment.value, __comment.set, None, None)

    
    # Attribute owner uses Python identifier owner
    __owner = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'owner'), 'owner', '__httpsubsonic_orgrestapi_Playlist_owner', pyxb.binding.datatypes.string)
    __owner._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 334, 8)
    __owner._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 334, 8)
    
    owner = property(__owner.value, __owner.set, None, None)

    
    # Attribute public uses Python identifier public
    __public = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'public'), 'public', '__httpsubsonic_orgrestapi_Playlist_public', pyxb.binding.datatypes.boolean)
    __public._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 335, 8)
    __public._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 335, 8)
    
    public = property(__public.value, __public.set, None, None)

    
    # Attribute songCount uses Python identifier songCount
    __songCount = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'songCount'), 'songCount', '__httpsubsonic_orgrestapi_Playlist_songCount', pyxb.binding.datatypes.int, required=True)
    __songCount._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 336, 8)
    __songCount._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 336, 8)
    
    songCount = property(__songCount.value, __songCount.set, None, None)

    
    # Attribute duration uses Python identifier duration
    __duration = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'duration'), 'duration', '__httpsubsonic_orgrestapi_Playlist_duration', pyxb.binding.datatypes.int, required=True)
    __duration._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 337, 8)
    __duration._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 337, 8)
    
    duration = property(__duration.value, __duration.set, None, None)

    
    # Attribute created uses Python identifier created
    __created = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'created'), 'created', '__httpsubsonic_orgrestapi_Playlist_created', pyxb.binding.datatypes.dateTime, required=True)
    __created._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 338, 8)
    __created._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 338, 8)
    
    created = property(__created.value, __created.set, None, None)

    
    # Attribute changed uses Python identifier changed
    __changed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'changed'), 'changed', '__httpsubsonic_orgrestapi_Playlist_changed', pyxb.binding.datatypes.dateTime, required=True)
    __changed._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 339, 8)
    __changed._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 339, 8)
    
    changed = property(__changed.value, __changed.set, None, None)

    
    # Attribute coverArt uses Python identifier coverArt
    __coverArt = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'coverArt'), 'coverArt', '__httpsubsonic_orgrestapi_Playlist_coverArt', pyxb.binding.datatypes.string)
    __coverArt._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 340, 8)
    __coverArt._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 340, 8)
    
    coverArt = property(__coverArt.value, __coverArt.set, None, None)

    _ElementMap.update({
        __allowedUser.name() : __allowedUser
    })
    _AttributeMap.update({
        __id.name() : __id,
        __name.name() : __name,
        __comment.name() : __comment,
        __owner.name() : __owner,
        __public.name() : __public,
        __songCount.name() : __songCount,
        __duration.name() : __duration,
        __created.name() : __created,
        __changed.name() : __changed,
        __coverArt.name() : __coverArt
    })
_module_typeBindings.Playlist = Playlist
Namespace.addCategoryObject('typeBinding', 'Playlist', Playlist)


# Complex type {http://subsonic.org/restapi}JukeboxStatus with content type EMPTY
class JukeboxStatus (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://subsonic.org/restapi}JukeboxStatus with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'JukeboxStatus')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 353, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute currentIndex uses Python identifier currentIndex
    __currentIndex = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'currentIndex'), 'currentIndex', '__httpsubsonic_orgrestapi_JukeboxStatus_currentIndex', pyxb.binding.datatypes.int, required=True)
    __currentIndex._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 354, 8)
    __currentIndex._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 354, 8)
    
    currentIndex = property(__currentIndex.value, __currentIndex.set, None, None)

    
    # Attribute playing uses Python identifier playing
    __playing = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'playing'), 'playing', '__httpsubsonic_orgrestapi_JukeboxStatus_playing', pyxb.binding.datatypes.boolean, required=True)
    __playing._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 355, 8)
    __playing._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 355, 8)
    
    playing = property(__playing.value, __playing.set, None, None)

    
    # Attribute gain uses Python identifier gain
    __gain = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'gain'), 'gain', '__httpsubsonic_orgrestapi_JukeboxStatus_gain', pyxb.binding.datatypes.float, required=True)
    __gain._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 356, 8)
    __gain._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 356, 8)
    
    gain = property(__gain.value, __gain.set, None, None)

    
    # Attribute position uses Python identifier position
    __position = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'position'), 'position', '__httpsubsonic_orgrestapi_JukeboxStatus_position', pyxb.binding.datatypes.int)
    __position._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 357, 8)
    __position._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 357, 8)
    
    position = property(__position.value, __position.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __currentIndex.name() : __currentIndex,
        __playing.name() : __playing,
        __gain.name() : __gain,
        __position.name() : __position
    })
_module_typeBindings.JukeboxStatus = JukeboxStatus
Namespace.addCategoryObject('typeBinding', 'JukeboxStatus', JukeboxStatus)


# Complex type {http://subsonic.org/restapi}ChatMessages with content type ELEMENT_ONLY
class ChatMessages (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://subsonic.org/restapi}ChatMessages with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ChatMessages')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 370, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://subsonic.org/restapi}chatMessage uses Python identifier chatMessage
    __chatMessage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'chatMessage'), 'chatMessage', '__httpsubsonic_orgrestapi_ChatMessages_httpsubsonic_orgrestapichatMessage', True, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 372, 12), )

    
    chatMessage = property(__chatMessage.value, __chatMessage.set, None, None)

    _ElementMap.update({
        __chatMessage.name() : __chatMessage
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ChatMessages = ChatMessages
Namespace.addCategoryObject('typeBinding', 'ChatMessages', ChatMessages)


# Complex type {http://subsonic.org/restapi}ChatMessage with content type EMPTY
class ChatMessage (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://subsonic.org/restapi}ChatMessage with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ChatMessage')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 376, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute username uses Python identifier username
    __username = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'username'), 'username', '__httpsubsonic_orgrestapi_ChatMessage_username', pyxb.binding.datatypes.string, required=True)
    __username._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 377, 8)
    __username._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 377, 8)
    
    username = property(__username.value, __username.set, None, None)

    
    # Attribute time uses Python identifier time
    __time = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'time'), 'time', '__httpsubsonic_orgrestapi_ChatMessage_time', pyxb.binding.datatypes.long, required=True)
    __time._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 378, 8)
    __time._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 378, 8)
    
    time = property(__time.value, __time.set, None, None)

    
    # Attribute message uses Python identifier message
    __message = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'message'), 'message', '__httpsubsonic_orgrestapi_ChatMessage_message', pyxb.binding.datatypes.string, required=True)
    __message._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 379, 8)
    __message._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 379, 8)
    
    message = property(__message.value, __message.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __username.name() : __username,
        __time.name() : __time,
        __message.name() : __message
    })
_module_typeBindings.ChatMessage = ChatMessage
Namespace.addCategoryObject('typeBinding', 'ChatMessage', ChatMessage)


# Complex type {http://subsonic.org/restapi}AlbumList with content type ELEMENT_ONLY
class AlbumList (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://subsonic.org/restapi}AlbumList with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AlbumList')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 382, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://subsonic.org/restapi}album uses Python identifier album
    __album = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'album'), 'album', '__httpsubsonic_orgrestapi_AlbumList_httpsubsonic_orgrestapialbum', True, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 384, 12), )

    
    album = property(__album.value, __album.set, None, None)

    _ElementMap.update({
        __album.name() : __album
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AlbumList = AlbumList
Namespace.addCategoryObject('typeBinding', 'AlbumList', AlbumList)


# Complex type {http://subsonic.org/restapi}AlbumList2 with content type ELEMENT_ONLY
class AlbumList2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://subsonic.org/restapi}AlbumList2 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AlbumList2')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 388, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://subsonic.org/restapi}album uses Python identifier album
    __album = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'album'), 'album', '__httpsubsonic_orgrestapi_AlbumList2_httpsubsonic_orgrestapialbum', True, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 390, 12), )

    
    album = property(__album.value, __album.set, None, None)

    _ElementMap.update({
        __album.name() : __album
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AlbumList2 = AlbumList2
Namespace.addCategoryObject('typeBinding', 'AlbumList2', AlbumList2)


# Complex type {http://subsonic.org/restapi}Songs with content type ELEMENT_ONLY
class Songs (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://subsonic.org/restapi}Songs with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Songs')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 394, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://subsonic.org/restapi}song uses Python identifier song
    __song = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'song'), 'song', '__httpsubsonic_orgrestapi_Songs_httpsubsonic_orgrestapisong', True, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 396, 12), )

    
    song = property(__song.value, __song.set, None, None)

    _ElementMap.update({
        __song.name() : __song
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Songs = Songs
Namespace.addCategoryObject('typeBinding', 'Songs', Songs)


# Complex type {http://subsonic.org/restapi}Lyrics with content type MIXED
class Lyrics (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://subsonic.org/restapi}Lyrics with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Lyrics')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 400, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute artist uses Python identifier artist
    __artist = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'artist'), 'artist', '__httpsubsonic_orgrestapi_Lyrics_artist', pyxb.binding.datatypes.string)
    __artist._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 401, 8)
    __artist._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 401, 8)
    
    artist = property(__artist.value, __artist.set, None, None)

    
    # Attribute title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'title'), 'title', '__httpsubsonic_orgrestapi_Lyrics_title', pyxb.binding.datatypes.string)
    __title._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 402, 8)
    __title._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 402, 8)
    
    title = property(__title.value, __title.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __artist.name() : __artist,
        __title.name() : __title
    })
_module_typeBindings.Lyrics = Lyrics
Namespace.addCategoryObject('typeBinding', 'Lyrics', Lyrics)


# Complex type {http://subsonic.org/restapi}Podcasts with content type ELEMENT_ONLY
class Podcasts (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://subsonic.org/restapi}Podcasts with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Podcasts')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 405, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://subsonic.org/restapi}channel uses Python identifier channel
    __channel = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'channel'), 'channel', '__httpsubsonic_orgrestapi_Podcasts_httpsubsonic_orgrestapichannel', True, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 407, 12), )

    
    channel = property(__channel.value, __channel.set, None, None)

    _ElementMap.update({
        __channel.name() : __channel
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Podcasts = Podcasts
Namespace.addCategoryObject('typeBinding', 'Podcasts', Podcasts)


# Complex type {http://subsonic.org/restapi}NewestPodcasts with content type ELEMENT_ONLY
class NewestPodcasts (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://subsonic.org/restapi}NewestPodcasts with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NewestPodcasts')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 425, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://subsonic.org/restapi}episode uses Python identifier episode
    __episode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'episode'), 'episode', '__httpsubsonic_orgrestapi_NewestPodcasts_httpsubsonic_orgrestapiepisode', True, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 427, 12), )

    
    episode = property(__episode.value, __episode.set, None, None)

    _ElementMap.update({
        __episode.name() : __episode
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.NewestPodcasts = NewestPodcasts
Namespace.addCategoryObject('typeBinding', 'NewestPodcasts', NewestPodcasts)


# Complex type {http://subsonic.org/restapi}InternetRadioStations with content type ELEMENT_ONLY
class InternetRadioStations (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://subsonic.org/restapi}InternetRadioStations with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InternetRadioStations')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 454, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://subsonic.org/restapi}internetRadioStation uses Python identifier internetRadioStation
    __internetRadioStation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'internetRadioStation'), 'internetRadioStation', '__httpsubsonic_orgrestapi_InternetRadioStations_httpsubsonic_orgrestapiinternetRadioStation', True, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 456, 12), )

    
    internetRadioStation = property(__internetRadioStation.value, __internetRadioStation.set, None, None)

    _ElementMap.update({
        __internetRadioStation.name() : __internetRadioStation
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.InternetRadioStations = InternetRadioStations
Namespace.addCategoryObject('typeBinding', 'InternetRadioStations', InternetRadioStations)


# Complex type {http://subsonic.org/restapi}InternetRadioStation with content type EMPTY
class InternetRadioStation (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://subsonic.org/restapi}InternetRadioStation with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InternetRadioStation')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 460, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpsubsonic_orgrestapi_InternetRadioStation_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 461, 8)
    __id._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 461, 8)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpsubsonic_orgrestapi_InternetRadioStation_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 462, 8)
    __name._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 462, 8)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute streamUrl uses Python identifier streamUrl
    __streamUrl = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'streamUrl'), 'streamUrl', '__httpsubsonic_orgrestapi_InternetRadioStation_streamUrl', pyxb.binding.datatypes.string, required=True)
    __streamUrl._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 463, 8)
    __streamUrl._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 463, 8)
    
    streamUrl = property(__streamUrl.value, __streamUrl.set, None, None)

    
    # Attribute homePageUrl uses Python identifier homePageUrl
    __homePageUrl = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'homePageUrl'), 'homePageUrl', '__httpsubsonic_orgrestapi_InternetRadioStation_homePageUrl', pyxb.binding.datatypes.string)
    __homePageUrl._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 464, 8)
    __homePageUrl._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 464, 8)
    
    homePageUrl = property(__homePageUrl.value, __homePageUrl.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __name.name() : __name,
        __streamUrl.name() : __streamUrl,
        __homePageUrl.name() : __homePageUrl
    })
_module_typeBindings.InternetRadioStation = InternetRadioStation
Namespace.addCategoryObject('typeBinding', 'InternetRadioStation', InternetRadioStation)


# Complex type {http://subsonic.org/restapi}Bookmarks with content type ELEMENT_ONLY
class Bookmarks (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://subsonic.org/restapi}Bookmarks with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Bookmarks')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 467, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://subsonic.org/restapi}bookmark uses Python identifier bookmark
    __bookmark = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'bookmark'), 'bookmark', '__httpsubsonic_orgrestapi_Bookmarks_httpsubsonic_orgrestapibookmark', True, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 469, 12), )

    
    bookmark = property(__bookmark.value, __bookmark.set, None, None)

    _ElementMap.update({
        __bookmark.name() : __bookmark
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Bookmarks = Bookmarks
Namespace.addCategoryObject('typeBinding', 'Bookmarks', Bookmarks)


# Complex type {http://subsonic.org/restapi}Bookmark with content type ELEMENT_ONLY
class Bookmark (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://subsonic.org/restapi}Bookmark with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Bookmark')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 473, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://subsonic.org/restapi}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'entry'), 'entry', '__httpsubsonic_orgrestapi_Bookmark_httpsubsonic_orgrestapientry', False, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 475, 12), )

    
    entry = property(__entry.value, __entry.set, None, None)

    
    # Attribute position uses Python identifier position
    __position = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'position'), 'position', '__httpsubsonic_orgrestapi_Bookmark_position', pyxb.binding.datatypes.long, required=True)
    __position._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 477, 8)
    __position._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 477, 8)
    
    position = property(__position.value, __position.set, None, None)

    
    # Attribute username uses Python identifier username
    __username = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'username'), 'username', '__httpsubsonic_orgrestapi_Bookmark_username', pyxb.binding.datatypes.string, required=True)
    __username._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 478, 8)
    __username._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 478, 8)
    
    username = property(__username.value, __username.set, None, None)

    
    # Attribute comment uses Python identifier comment
    __comment = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'comment'), 'comment', '__httpsubsonic_orgrestapi_Bookmark_comment', pyxb.binding.datatypes.string)
    __comment._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 479, 8)
    __comment._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 479, 8)
    
    comment = property(__comment.value, __comment.set, None, None)

    
    # Attribute created uses Python identifier created
    __created = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'created'), 'created', '__httpsubsonic_orgrestapi_Bookmark_created', pyxb.binding.datatypes.dateTime, required=True)
    __created._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 480, 8)
    __created._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 480, 8)
    
    created = property(__created.value, __created.set, None, None)

    
    # Attribute changed uses Python identifier changed
    __changed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'changed'), 'changed', '__httpsubsonic_orgrestapi_Bookmark_changed', pyxb.binding.datatypes.dateTime, required=True)
    __changed._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 481, 8)
    __changed._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 481, 8)
    
    changed = property(__changed.value, __changed.set, None, None)

    _ElementMap.update({
        __entry.name() : __entry
    })
    _AttributeMap.update({
        __position.name() : __position,
        __username.name() : __username,
        __comment.name() : __comment,
        __created.name() : __created,
        __changed.name() : __changed
    })
_module_typeBindings.Bookmark = Bookmark
Namespace.addCategoryObject('typeBinding', 'Bookmark', Bookmark)


# Complex type {http://subsonic.org/restapi}PlayQueue with content type ELEMENT_ONLY
class PlayQueue (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://subsonic.org/restapi}PlayQueue with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PlayQueue')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 484, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://subsonic.org/restapi}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'entry'), 'entry', '__httpsubsonic_orgrestapi_PlayQueue_httpsubsonic_orgrestapientry', True, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 486, 12), )

    
    entry = property(__entry.value, __entry.set, None, None)

    
    # Attribute current uses Python identifier current
    __current = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'current'), 'current', '__httpsubsonic_orgrestapi_PlayQueue_current', pyxb.binding.datatypes.int)
    __current._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 488, 8)
    __current._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 488, 8)
    
    current = property(__current.value, __current.set, None, None)

    
    # Attribute position uses Python identifier position
    __position = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'position'), 'position', '__httpsubsonic_orgrestapi_PlayQueue_position', pyxb.binding.datatypes.long)
    __position._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 489, 8)
    __position._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 489, 8)
    
    position = property(__position.value, __position.set, None, None)

    
    # Attribute username uses Python identifier username
    __username = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'username'), 'username', '__httpsubsonic_orgrestapi_PlayQueue_username', pyxb.binding.datatypes.string, required=True)
    __username._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 490, 8)
    __username._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 490, 8)
    
    username = property(__username.value, __username.set, None, None)

    
    # Attribute changed uses Python identifier changed
    __changed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'changed'), 'changed', '__httpsubsonic_orgrestapi_PlayQueue_changed', pyxb.binding.datatypes.dateTime, required=True)
    __changed._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 491, 8)
    __changed._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 491, 8)
    
    changed = property(__changed.value, __changed.set, None, None)

    
    # Attribute changedBy uses Python identifier changedBy
    __changedBy = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'changedBy'), 'changedBy', '__httpsubsonic_orgrestapi_PlayQueue_changedBy', pyxb.binding.datatypes.string, required=True)
    __changedBy._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 492, 8)
    __changedBy._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 492, 8)
    
    changedBy = property(__changedBy.value, __changedBy.set, None, None)

    _ElementMap.update({
        __entry.name() : __entry
    })
    _AttributeMap.update({
        __current.name() : __current,
        __position.name() : __position,
        __username.name() : __username,
        __changed.name() : __changed,
        __changedBy.name() : __changedBy
    })
_module_typeBindings.PlayQueue = PlayQueue
Namespace.addCategoryObject('typeBinding', 'PlayQueue', PlayQueue)


# Complex type {http://subsonic.org/restapi}Shares with content type ELEMENT_ONLY
class Shares (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://subsonic.org/restapi}Shares with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Shares')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 495, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://subsonic.org/restapi}share uses Python identifier share
    __share = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'share'), 'share', '__httpsubsonic_orgrestapi_Shares_httpsubsonic_orgrestapishare', True, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 497, 12), )

    
    share = property(__share.value, __share.set, None, None)

    _ElementMap.update({
        __share.name() : __share
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Shares = Shares
Namespace.addCategoryObject('typeBinding', 'Shares', Shares)


# Complex type {http://subsonic.org/restapi}Share with content type ELEMENT_ONLY
class Share (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://subsonic.org/restapi}Share with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Share')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 501, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://subsonic.org/restapi}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'entry'), 'entry', '__httpsubsonic_orgrestapi_Share_httpsubsonic_orgrestapientry', True, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 503, 12), )

    
    entry = property(__entry.value, __entry.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpsubsonic_orgrestapi_Share_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 505, 8)
    __id._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 505, 8)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute url uses Python identifier url
    __url = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'url'), 'url', '__httpsubsonic_orgrestapi_Share_url', pyxb.binding.datatypes.string, required=True)
    __url._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 506, 8)
    __url._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 506, 8)
    
    url = property(__url.value, __url.set, None, None)

    
    # Attribute description uses Python identifier description
    __description = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'description'), 'description', '__httpsubsonic_orgrestapi_Share_description', pyxb.binding.datatypes.string)
    __description._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 507, 8)
    __description._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 507, 8)
    
    description = property(__description.value, __description.set, None, None)

    
    # Attribute username uses Python identifier username
    __username = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'username'), 'username', '__httpsubsonic_orgrestapi_Share_username', pyxb.binding.datatypes.string, required=True)
    __username._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 508, 8)
    __username._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 508, 8)
    
    username = property(__username.value, __username.set, None, None)

    
    # Attribute created uses Python identifier created
    __created = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'created'), 'created', '__httpsubsonic_orgrestapi_Share_created', pyxb.binding.datatypes.dateTime, required=True)
    __created._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 509, 8)
    __created._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 509, 8)
    
    created = property(__created.value, __created.set, None, None)

    
    # Attribute expires uses Python identifier expires
    __expires = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'expires'), 'expires', '__httpsubsonic_orgrestapi_Share_expires', pyxb.binding.datatypes.dateTime)
    __expires._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 510, 8)
    __expires._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 510, 8)
    
    expires = property(__expires.value, __expires.set, None, None)

    
    # Attribute lastVisited uses Python identifier lastVisited
    __lastVisited = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lastVisited'), 'lastVisited', '__httpsubsonic_orgrestapi_Share_lastVisited', pyxb.binding.datatypes.dateTime)
    __lastVisited._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 511, 8)
    __lastVisited._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 511, 8)
    
    lastVisited = property(__lastVisited.value, __lastVisited.set, None, None)

    
    # Attribute visitCount uses Python identifier visitCount
    __visitCount = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'visitCount'), 'visitCount', '__httpsubsonic_orgrestapi_Share_visitCount', pyxb.binding.datatypes.int, required=True)
    __visitCount._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 512, 8)
    __visitCount._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 512, 8)
    
    visitCount = property(__visitCount.value, __visitCount.set, None, None)

    _ElementMap.update({
        __entry.name() : __entry
    })
    _AttributeMap.update({
        __id.name() : __id,
        __url.name() : __url,
        __description.name() : __description,
        __username.name() : __username,
        __created.name() : __created,
        __expires.name() : __expires,
        __lastVisited.name() : __lastVisited,
        __visitCount.name() : __visitCount
    })
_module_typeBindings.Share = Share
Namespace.addCategoryObject('typeBinding', 'Share', Share)


# Complex type {http://subsonic.org/restapi}Starred with content type ELEMENT_ONLY
class Starred (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://subsonic.org/restapi}Starred with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Starred')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 515, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://subsonic.org/restapi}artist uses Python identifier artist
    __artist = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'artist'), 'artist', '__httpsubsonic_orgrestapi_Starred_httpsubsonic_orgrestapiartist', True, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 517, 12), )

    
    artist = property(__artist.value, __artist.set, None, None)

    
    # Element {http://subsonic.org/restapi}album uses Python identifier album
    __album = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'album'), 'album', '__httpsubsonic_orgrestapi_Starred_httpsubsonic_orgrestapialbum', True, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 518, 12), )

    
    album = property(__album.value, __album.set, None, None)

    
    # Element {http://subsonic.org/restapi}song uses Python identifier song
    __song = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'song'), 'song', '__httpsubsonic_orgrestapi_Starred_httpsubsonic_orgrestapisong', True, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 519, 12), )

    
    song = property(__song.value, __song.set, None, None)

    _ElementMap.update({
        __artist.name() : __artist,
        __album.name() : __album,
        __song.name() : __song
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Starred = Starred
Namespace.addCategoryObject('typeBinding', 'Starred', Starred)


# Complex type {http://subsonic.org/restapi}AlbumInfo with content type ELEMENT_ONLY
class AlbumInfo (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://subsonic.org/restapi}AlbumInfo with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AlbumInfo')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 523, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://subsonic.org/restapi}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'notes'), 'notes', '__httpsubsonic_orgrestapi_AlbumInfo_httpsubsonic_orgrestapinotes', False, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 525, 12), )

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element {http://subsonic.org/restapi}musicBrainzId uses Python identifier musicBrainzId
    __musicBrainzId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'musicBrainzId'), 'musicBrainzId', '__httpsubsonic_orgrestapi_AlbumInfo_httpsubsonic_orgrestapimusicBrainzId', False, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 526, 12), )

    
    musicBrainzId = property(__musicBrainzId.value, __musicBrainzId.set, None, None)

    
    # Element {http://subsonic.org/restapi}lastFmUrl uses Python identifier lastFmUrl
    __lastFmUrl = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lastFmUrl'), 'lastFmUrl', '__httpsubsonic_orgrestapi_AlbumInfo_httpsubsonic_orgrestapilastFmUrl', False, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 527, 12), )

    
    lastFmUrl = property(__lastFmUrl.value, __lastFmUrl.set, None, None)

    
    # Element {http://subsonic.org/restapi}smallImageUrl uses Python identifier smallImageUrl
    __smallImageUrl = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'smallImageUrl'), 'smallImageUrl', '__httpsubsonic_orgrestapi_AlbumInfo_httpsubsonic_orgrestapismallImageUrl', False, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 528, 12), )

    
    smallImageUrl = property(__smallImageUrl.value, __smallImageUrl.set, None, None)

    
    # Element {http://subsonic.org/restapi}mediumImageUrl uses Python identifier mediumImageUrl
    __mediumImageUrl = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'mediumImageUrl'), 'mediumImageUrl', '__httpsubsonic_orgrestapi_AlbumInfo_httpsubsonic_orgrestapimediumImageUrl', False, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 529, 12), )

    
    mediumImageUrl = property(__mediumImageUrl.value, __mediumImageUrl.set, None, None)

    
    # Element {http://subsonic.org/restapi}largeImageUrl uses Python identifier largeImageUrl
    __largeImageUrl = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'largeImageUrl'), 'largeImageUrl', '__httpsubsonic_orgrestapi_AlbumInfo_httpsubsonic_orgrestapilargeImageUrl', False, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 530, 12), )

    
    largeImageUrl = property(__largeImageUrl.value, __largeImageUrl.set, None, None)

    _ElementMap.update({
        __notes.name() : __notes,
        __musicBrainzId.name() : __musicBrainzId,
        __lastFmUrl.name() : __lastFmUrl,
        __smallImageUrl.name() : __smallImageUrl,
        __mediumImageUrl.name() : __mediumImageUrl,
        __largeImageUrl.name() : __largeImageUrl
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AlbumInfo = AlbumInfo
Namespace.addCategoryObject('typeBinding', 'AlbumInfo', AlbumInfo)


# Complex type {http://subsonic.org/restapi}ArtistInfoBase with content type ELEMENT_ONLY
class ArtistInfoBase (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://subsonic.org/restapi}ArtistInfoBase with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ArtistInfoBase')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 534, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://subsonic.org/restapi}biography uses Python identifier biography
    __biography = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'biography'), 'biography', '__httpsubsonic_orgrestapi_ArtistInfoBase_httpsubsonic_orgrestapibiography', False, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 536, 12), )

    
    biography = property(__biography.value, __biography.set, None, None)

    
    # Element {http://subsonic.org/restapi}musicBrainzId uses Python identifier musicBrainzId
    __musicBrainzId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'musicBrainzId'), 'musicBrainzId', '__httpsubsonic_orgrestapi_ArtistInfoBase_httpsubsonic_orgrestapimusicBrainzId', False, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 537, 12), )

    
    musicBrainzId = property(__musicBrainzId.value, __musicBrainzId.set, None, None)

    
    # Element {http://subsonic.org/restapi}lastFmUrl uses Python identifier lastFmUrl
    __lastFmUrl = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lastFmUrl'), 'lastFmUrl', '__httpsubsonic_orgrestapi_ArtistInfoBase_httpsubsonic_orgrestapilastFmUrl', False, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 538, 12), )

    
    lastFmUrl = property(__lastFmUrl.value, __lastFmUrl.set, None, None)

    
    # Element {http://subsonic.org/restapi}smallImageUrl uses Python identifier smallImageUrl
    __smallImageUrl = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'smallImageUrl'), 'smallImageUrl', '__httpsubsonic_orgrestapi_ArtistInfoBase_httpsubsonic_orgrestapismallImageUrl', False, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 539, 12), )

    
    smallImageUrl = property(__smallImageUrl.value, __smallImageUrl.set, None, None)

    
    # Element {http://subsonic.org/restapi}mediumImageUrl uses Python identifier mediumImageUrl
    __mediumImageUrl = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'mediumImageUrl'), 'mediumImageUrl', '__httpsubsonic_orgrestapi_ArtistInfoBase_httpsubsonic_orgrestapimediumImageUrl', False, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 540, 12), )

    
    mediumImageUrl = property(__mediumImageUrl.value, __mediumImageUrl.set, None, None)

    
    # Element {http://subsonic.org/restapi}largeImageUrl uses Python identifier largeImageUrl
    __largeImageUrl = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'largeImageUrl'), 'largeImageUrl', '__httpsubsonic_orgrestapi_ArtistInfoBase_httpsubsonic_orgrestapilargeImageUrl', False, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 541, 12), )

    
    largeImageUrl = property(__largeImageUrl.value, __largeImageUrl.set, None, None)

    _ElementMap.update({
        __biography.name() : __biography,
        __musicBrainzId.name() : __musicBrainzId,
        __lastFmUrl.name() : __lastFmUrl,
        __smallImageUrl.name() : __smallImageUrl,
        __mediumImageUrl.name() : __mediumImageUrl,
        __largeImageUrl.name() : __largeImageUrl
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ArtistInfoBase = ArtistInfoBase
Namespace.addCategoryObject('typeBinding', 'ArtistInfoBase', ArtistInfoBase)


# Complex type {http://subsonic.org/restapi}SimilarSongs with content type ELEMENT_ONLY
class SimilarSongs (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://subsonic.org/restapi}SimilarSongs with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SimilarSongs')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 565, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://subsonic.org/restapi}song uses Python identifier song
    __song = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'song'), 'song', '__httpsubsonic_orgrestapi_SimilarSongs_httpsubsonic_orgrestapisong', True, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 567, 12), )

    
    song = property(__song.value, __song.set, None, None)

    _ElementMap.update({
        __song.name() : __song
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SimilarSongs = SimilarSongs
Namespace.addCategoryObject('typeBinding', 'SimilarSongs', SimilarSongs)


# Complex type {http://subsonic.org/restapi}SimilarSongs2 with content type ELEMENT_ONLY
class SimilarSongs2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://subsonic.org/restapi}SimilarSongs2 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SimilarSongs2')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 571, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://subsonic.org/restapi}song uses Python identifier song
    __song = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'song'), 'song', '__httpsubsonic_orgrestapi_SimilarSongs2_httpsubsonic_orgrestapisong', True, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 573, 12), )

    
    song = property(__song.value, __song.set, None, None)

    _ElementMap.update({
        __song.name() : __song
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SimilarSongs2 = SimilarSongs2
Namespace.addCategoryObject('typeBinding', 'SimilarSongs2', SimilarSongs2)


# Complex type {http://subsonic.org/restapi}TopSongs with content type ELEMENT_ONLY
class TopSongs (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://subsonic.org/restapi}TopSongs with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TopSongs')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 577, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://subsonic.org/restapi}song uses Python identifier song
    __song = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'song'), 'song', '__httpsubsonic_orgrestapi_TopSongs_httpsubsonic_orgrestapisong', True, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 579, 12), )

    
    song = property(__song.value, __song.set, None, None)

    _ElementMap.update({
        __song.name() : __song
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TopSongs = TopSongs
Namespace.addCategoryObject('typeBinding', 'TopSongs', TopSongs)


# Complex type {http://subsonic.org/restapi}Starred2 with content type ELEMENT_ONLY
class Starred2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://subsonic.org/restapi}Starred2 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Starred2')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 583, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://subsonic.org/restapi}artist uses Python identifier artist
    __artist = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'artist'), 'artist', '__httpsubsonic_orgrestapi_Starred2_httpsubsonic_orgrestapiartist', True, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 585, 12), )

    
    artist = property(__artist.value, __artist.set, None, None)

    
    # Element {http://subsonic.org/restapi}album uses Python identifier album
    __album = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'album'), 'album', '__httpsubsonic_orgrestapi_Starred2_httpsubsonic_orgrestapialbum', True, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 586, 12), )

    
    album = property(__album.value, __album.set, None, None)

    
    # Element {http://subsonic.org/restapi}song uses Python identifier song
    __song = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'song'), 'song', '__httpsubsonic_orgrestapi_Starred2_httpsubsonic_orgrestapisong', True, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 587, 12), )

    
    song = property(__song.value, __song.set, None, None)

    _ElementMap.update({
        __artist.name() : __artist,
        __album.name() : __album,
        __song.name() : __song
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Starred2 = Starred2
Namespace.addCategoryObject('typeBinding', 'Starred2', Starred2)


# Complex type {http://subsonic.org/restapi}License with content type EMPTY
class License (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://subsonic.org/restapi}License with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'License')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 591, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute valid uses Python identifier valid
    __valid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'valid'), 'valid', '__httpsubsonic_orgrestapi_License_valid', pyxb.binding.datatypes.boolean, required=True)
    __valid._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 592, 8)
    __valid._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 592, 8)
    
    valid = property(__valid.value, __valid.set, None, None)

    
    # Attribute email uses Python identifier email
    __email = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'email'), 'email', '__httpsubsonic_orgrestapi_License_email', pyxb.binding.datatypes.string)
    __email._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 593, 8)
    __email._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 593, 8)
    
    email = property(__email.value, __email.set, None, None)

    
    # Attribute licenseExpires uses Python identifier licenseExpires
    __licenseExpires = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'licenseExpires'), 'licenseExpires', '__httpsubsonic_orgrestapi_License_licenseExpires', pyxb.binding.datatypes.dateTime)
    __licenseExpires._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 594, 8)
    __licenseExpires._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 594, 8)
    
    licenseExpires = property(__licenseExpires.value, __licenseExpires.set, None, None)

    
    # Attribute trialExpires uses Python identifier trialExpires
    __trialExpires = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'trialExpires'), 'trialExpires', '__httpsubsonic_orgrestapi_License_trialExpires', pyxb.binding.datatypes.dateTime)
    __trialExpires._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 595, 8)
    __trialExpires._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 595, 8)
    
    trialExpires = property(__trialExpires.value, __trialExpires.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __valid.name() : __valid,
        __email.name() : __email,
        __licenseExpires.name() : __licenseExpires,
        __trialExpires.name() : __trialExpires
    })
_module_typeBindings.License = License
Namespace.addCategoryObject('typeBinding', 'License', License)


# Complex type {http://subsonic.org/restapi}Users with content type ELEMENT_ONLY
class Users (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://subsonic.org/restapi}Users with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Users')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 598, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://subsonic.org/restapi}user uses Python identifier user
    __user = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'user'), 'user', '__httpsubsonic_orgrestapi_Users_httpsubsonic_orgrestapiuser', True, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 600, 12), )

    
    user = property(__user.value, __user.set, None, None)

    _ElementMap.update({
        __user.name() : __user
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Users = Users
Namespace.addCategoryObject('typeBinding', 'Users', Users)


# Complex type {http://subsonic.org/restapi}User with content type ELEMENT_ONLY
class User (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://subsonic.org/restapi}User with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'User')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 604, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://subsonic.org/restapi}folder uses Python identifier folder
    __folder = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'folder'), 'folder', '__httpsubsonic_orgrestapi_User_httpsubsonic_orgrestapifolder', True, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 606, 12), )

    
    folder = property(__folder.value, __folder.set, None, None)

    
    # Attribute username uses Python identifier username
    __username = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'username'), 'username', '__httpsubsonic_orgrestapi_User_username', pyxb.binding.datatypes.string, required=True)
    __username._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 608, 8)
    __username._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 608, 8)
    
    username = property(__username.value, __username.set, None, None)

    
    # Attribute email uses Python identifier email
    __email = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'email'), 'email', '__httpsubsonic_orgrestapi_User_email', pyxb.binding.datatypes.string)
    __email._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 609, 8)
    __email._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 609, 8)
    
    email = property(__email.value, __email.set, None, None)

    
    # Attribute scrobblingEnabled uses Python identifier scrobblingEnabled
    __scrobblingEnabled = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'scrobblingEnabled'), 'scrobblingEnabled', '__httpsubsonic_orgrestapi_User_scrobblingEnabled', pyxb.binding.datatypes.boolean, required=True)
    __scrobblingEnabled._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 610, 8)
    __scrobblingEnabled._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 610, 8)
    
    scrobblingEnabled = property(__scrobblingEnabled.value, __scrobblingEnabled.set, None, None)

    
    # Attribute maxBitRate uses Python identifier maxBitRate
    __maxBitRate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'maxBitRate'), 'maxBitRate', '__httpsubsonic_orgrestapi_User_maxBitRate', pyxb.binding.datatypes.int)
    __maxBitRate._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 611, 8)
    __maxBitRate._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 611, 8)
    
    maxBitRate = property(__maxBitRate.value, __maxBitRate.set, None, None)

    
    # Attribute adminRole uses Python identifier adminRole
    __adminRole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'adminRole'), 'adminRole', '__httpsubsonic_orgrestapi_User_adminRole', pyxb.binding.datatypes.boolean, required=True)
    __adminRole._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 612, 8)
    __adminRole._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 612, 8)
    
    adminRole = property(__adminRole.value, __adminRole.set, None, None)

    
    # Attribute settingsRole uses Python identifier settingsRole
    __settingsRole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'settingsRole'), 'settingsRole', '__httpsubsonic_orgrestapi_User_settingsRole', pyxb.binding.datatypes.boolean, required=True)
    __settingsRole._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 613, 8)
    __settingsRole._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 613, 8)
    
    settingsRole = property(__settingsRole.value, __settingsRole.set, None, None)

    
    # Attribute downloadRole uses Python identifier downloadRole
    __downloadRole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'downloadRole'), 'downloadRole', '__httpsubsonic_orgrestapi_User_downloadRole', pyxb.binding.datatypes.boolean, required=True)
    __downloadRole._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 614, 8)
    __downloadRole._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 614, 8)
    
    downloadRole = property(__downloadRole.value, __downloadRole.set, None, None)

    
    # Attribute uploadRole uses Python identifier uploadRole
    __uploadRole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uploadRole'), 'uploadRole', '__httpsubsonic_orgrestapi_User_uploadRole', pyxb.binding.datatypes.boolean, required=True)
    __uploadRole._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 615, 8)
    __uploadRole._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 615, 8)
    
    uploadRole = property(__uploadRole.value, __uploadRole.set, None, None)

    
    # Attribute playlistRole uses Python identifier playlistRole
    __playlistRole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'playlistRole'), 'playlistRole', '__httpsubsonic_orgrestapi_User_playlistRole', pyxb.binding.datatypes.boolean, required=True)
    __playlistRole._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 616, 8)
    __playlistRole._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 616, 8)
    
    playlistRole = property(__playlistRole.value, __playlistRole.set, None, None)

    
    # Attribute coverArtRole uses Python identifier coverArtRole
    __coverArtRole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'coverArtRole'), 'coverArtRole', '__httpsubsonic_orgrestapi_User_coverArtRole', pyxb.binding.datatypes.boolean, required=True)
    __coverArtRole._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 617, 8)
    __coverArtRole._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 617, 8)
    
    coverArtRole = property(__coverArtRole.value, __coverArtRole.set, None, None)

    
    # Attribute commentRole uses Python identifier commentRole
    __commentRole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'commentRole'), 'commentRole', '__httpsubsonic_orgrestapi_User_commentRole', pyxb.binding.datatypes.boolean, required=True)
    __commentRole._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 618, 8)
    __commentRole._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 618, 8)
    
    commentRole = property(__commentRole.value, __commentRole.set, None, None)

    
    # Attribute podcastRole uses Python identifier podcastRole
    __podcastRole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'podcastRole'), 'podcastRole', '__httpsubsonic_orgrestapi_User_podcastRole', pyxb.binding.datatypes.boolean, required=True)
    __podcastRole._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 619, 8)
    __podcastRole._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 619, 8)
    
    podcastRole = property(__podcastRole.value, __podcastRole.set, None, None)

    
    # Attribute streamRole uses Python identifier streamRole
    __streamRole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'streamRole'), 'streamRole', '__httpsubsonic_orgrestapi_User_streamRole', pyxb.binding.datatypes.boolean, required=True)
    __streamRole._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 620, 8)
    __streamRole._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 620, 8)
    
    streamRole = property(__streamRole.value, __streamRole.set, None, None)

    
    # Attribute jukeboxRole uses Python identifier jukeboxRole
    __jukeboxRole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'jukeboxRole'), 'jukeboxRole', '__httpsubsonic_orgrestapi_User_jukeboxRole', pyxb.binding.datatypes.boolean, required=True)
    __jukeboxRole._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 621, 8)
    __jukeboxRole._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 621, 8)
    
    jukeboxRole = property(__jukeboxRole.value, __jukeboxRole.set, None, None)

    
    # Attribute shareRole uses Python identifier shareRole
    __shareRole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'shareRole'), 'shareRole', '__httpsubsonic_orgrestapi_User_shareRole', pyxb.binding.datatypes.boolean, required=True)
    __shareRole._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 622, 8)
    __shareRole._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 622, 8)
    
    shareRole = property(__shareRole.value, __shareRole.set, None, None)

    
    # Attribute videoConversionRole uses Python identifier videoConversionRole
    __videoConversionRole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'videoConversionRole'), 'videoConversionRole', '__httpsubsonic_orgrestapi_User_videoConversionRole', pyxb.binding.datatypes.boolean, required=True)
    __videoConversionRole._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 623, 8)
    __videoConversionRole._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 623, 8)
    
    videoConversionRole = property(__videoConversionRole.value, __videoConversionRole.set, None, None)

    
    # Attribute avatarLastChanged uses Python identifier avatarLastChanged
    __avatarLastChanged = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'avatarLastChanged'), 'avatarLastChanged', '__httpsubsonic_orgrestapi_User_avatarLastChanged', pyxb.binding.datatypes.dateTime)
    __avatarLastChanged._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 624, 8)
    __avatarLastChanged._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 624, 8)
    
    avatarLastChanged = property(__avatarLastChanged.value, __avatarLastChanged.set, None, None)

    _ElementMap.update({
        __folder.name() : __folder
    })
    _AttributeMap.update({
        __username.name() : __username,
        __email.name() : __email,
        __scrobblingEnabled.name() : __scrobblingEnabled,
        __maxBitRate.name() : __maxBitRate,
        __adminRole.name() : __adminRole,
        __settingsRole.name() : __settingsRole,
        __downloadRole.name() : __downloadRole,
        __uploadRole.name() : __uploadRole,
        __playlistRole.name() : __playlistRole,
        __coverArtRole.name() : __coverArtRole,
        __commentRole.name() : __commentRole,
        __podcastRole.name() : __podcastRole,
        __streamRole.name() : __streamRole,
        __jukeboxRole.name() : __jukeboxRole,
        __shareRole.name() : __shareRole,
        __videoConversionRole.name() : __videoConversionRole,
        __avatarLastChanged.name() : __avatarLastChanged
    })
_module_typeBindings.User = User
Namespace.addCategoryObject('typeBinding', 'User', User)


# Complex type {http://subsonic.org/restapi}Error with content type EMPTY
class Error (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://subsonic.org/restapi}Error with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Error')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 627, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute code uses Python identifier code
    __code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'code'), 'code', '__httpsubsonic_orgrestapi_Error_code', pyxb.binding.datatypes.int, required=True)
    __code._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 628, 8)
    __code._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 628, 8)
    
    code = property(__code.value, __code.set, None, None)

    
    # Attribute message uses Python identifier message
    __message = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'message'), 'message', '__httpsubsonic_orgrestapi_Error_message', pyxb.binding.datatypes.string)
    __message._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 629, 8)
    __message._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 629, 8)
    
    message = property(__message.value, __message.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __code.name() : __code,
        __message.name() : __message
    })
_module_typeBindings.Error = Error
Namespace.addCategoryObject('typeBinding', 'Error', Error)


# Complex type {http://subsonic.org/restapi}Response with content type ELEMENT_ONLY
class Response (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://subsonic.org/restapi}Response with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Response')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 11, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://subsonic.org/restapi}musicFolders uses Python identifier musicFolders
    __musicFolders = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'musicFolders'), 'musicFolders', '__httpsubsonic_orgrestapi_Response_httpsubsonic_orgrestapimusicFolders', False, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 13, 12), )

    
    musicFolders = property(__musicFolders.value, __musicFolders.set, None, None)

    
    # Element {http://subsonic.org/restapi}indexes uses Python identifier indexes
    __indexes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'indexes'), 'indexes', '__httpsubsonic_orgrestapi_Response_httpsubsonic_orgrestapiindexes', False, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 14, 12), )

    
    indexes = property(__indexes.value, __indexes.set, None, None)

    
    # Element {http://subsonic.org/restapi}directory uses Python identifier directory
    __directory = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'directory'), 'directory', '__httpsubsonic_orgrestapi_Response_httpsubsonic_orgrestapidirectory', False, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 15, 12), )

    
    directory = property(__directory.value, __directory.set, None, None)

    
    # Element {http://subsonic.org/restapi}genres uses Python identifier genres
    __genres = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'genres'), 'genres', '__httpsubsonic_orgrestapi_Response_httpsubsonic_orgrestapigenres', False, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 16, 12), )

    
    genres = property(__genres.value, __genres.set, None, None)

    
    # Element {http://subsonic.org/restapi}artists uses Python identifier artists
    __artists = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'artists'), 'artists', '__httpsubsonic_orgrestapi_Response_httpsubsonic_orgrestapiartists', False, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 17, 12), )

    
    artists = property(__artists.value, __artists.set, None, None)

    
    # Element {http://subsonic.org/restapi}artist uses Python identifier artist
    __artist = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'artist'), 'artist', '__httpsubsonic_orgrestapi_Response_httpsubsonic_orgrestapiartist', False, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 18, 12), )

    
    artist = property(__artist.value, __artist.set, None, None)

    
    # Element {http://subsonic.org/restapi}album uses Python identifier album
    __album = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'album'), 'album', '__httpsubsonic_orgrestapi_Response_httpsubsonic_orgrestapialbum', False, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 19, 12), )

    
    album = property(__album.value, __album.set, None, None)

    
    # Element {http://subsonic.org/restapi}song uses Python identifier song
    __song = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'song'), 'song', '__httpsubsonic_orgrestapi_Response_httpsubsonic_orgrestapisong', False, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 20, 12), )

    
    song = property(__song.value, __song.set, None, None)

    
    # Element {http://subsonic.org/restapi}videos uses Python identifier videos
    __videos = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'videos'), 'videos', '__httpsubsonic_orgrestapi_Response_httpsubsonic_orgrestapivideos', False, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 21, 12), )

    
    videos = property(__videos.value, __videos.set, None, None)

    
    # Element {http://subsonic.org/restapi}videoInfo uses Python identifier videoInfo
    __videoInfo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'videoInfo'), 'videoInfo', '__httpsubsonic_orgrestapi_Response_httpsubsonic_orgrestapivideoInfo', False, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 22, 12), )

    
    videoInfo = property(__videoInfo.value, __videoInfo.set, None, None)

    
    # Element {http://subsonic.org/restapi}nowPlaying uses Python identifier nowPlaying
    __nowPlaying = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'nowPlaying'), 'nowPlaying', '__httpsubsonic_orgrestapi_Response_httpsubsonic_orgrestapinowPlaying', False, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 23, 12), )

    
    nowPlaying = property(__nowPlaying.value, __nowPlaying.set, None, None)

    
    # Element {http://subsonic.org/restapi}searchResult uses Python identifier searchResult
    __searchResult = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'searchResult'), 'searchResult', '__httpsubsonic_orgrestapi_Response_httpsubsonic_orgrestapisearchResult', False, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 24, 12), )

    
    searchResult = property(__searchResult.value, __searchResult.set, None, None)

    
    # Element {http://subsonic.org/restapi}searchResult2 uses Python identifier searchResult2
    __searchResult2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'searchResult2'), 'searchResult2', '__httpsubsonic_orgrestapi_Response_httpsubsonic_orgrestapisearchResult2', False, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 25, 12), )

    
    searchResult2 = property(__searchResult2.value, __searchResult2.set, None, None)

    
    # Element {http://subsonic.org/restapi}searchResult3 uses Python identifier searchResult3
    __searchResult3 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'searchResult3'), 'searchResult3', '__httpsubsonic_orgrestapi_Response_httpsubsonic_orgrestapisearchResult3', False, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 26, 12), )

    
    searchResult3 = property(__searchResult3.value, __searchResult3.set, None, None)

    
    # Element {http://subsonic.org/restapi}playlists uses Python identifier playlists
    __playlists = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'playlists'), 'playlists', '__httpsubsonic_orgrestapi_Response_httpsubsonic_orgrestapiplaylists', False, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 27, 12), )

    
    playlists = property(__playlists.value, __playlists.set, None, None)

    
    # Element {http://subsonic.org/restapi}playlist uses Python identifier playlist
    __playlist = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'playlist'), 'playlist', '__httpsubsonic_orgrestapi_Response_httpsubsonic_orgrestapiplaylist', False, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 28, 12), )

    
    playlist = property(__playlist.value, __playlist.set, None, None)

    
    # Element {http://subsonic.org/restapi}jukeboxStatus uses Python identifier jukeboxStatus
    __jukeboxStatus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'jukeboxStatus'), 'jukeboxStatus', '__httpsubsonic_orgrestapi_Response_httpsubsonic_orgrestapijukeboxStatus', False, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 29, 12), )

    
    jukeboxStatus = property(__jukeboxStatus.value, __jukeboxStatus.set, None, None)

    
    # Element {http://subsonic.org/restapi}jukeboxPlaylist uses Python identifier jukeboxPlaylist
    __jukeboxPlaylist = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'jukeboxPlaylist'), 'jukeboxPlaylist', '__httpsubsonic_orgrestapi_Response_httpsubsonic_orgrestapijukeboxPlaylist', False, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 30, 12), )

    
    jukeboxPlaylist = property(__jukeboxPlaylist.value, __jukeboxPlaylist.set, None, None)

    
    # Element {http://subsonic.org/restapi}license uses Python identifier license
    __license = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'license'), 'license', '__httpsubsonic_orgrestapi_Response_httpsubsonic_orgrestapilicense', False, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 31, 12), )

    
    license = property(__license.value, __license.set, None, None)

    
    # Element {http://subsonic.org/restapi}users uses Python identifier users
    __users = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'users'), 'users', '__httpsubsonic_orgrestapi_Response_httpsubsonic_orgrestapiusers', False, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 32, 12), )

    
    users = property(__users.value, __users.set, None, None)

    
    # Element {http://subsonic.org/restapi}user uses Python identifier user
    __user = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'user'), 'user', '__httpsubsonic_orgrestapi_Response_httpsubsonic_orgrestapiuser', False, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 33, 12), )

    
    user = property(__user.value, __user.set, None, None)

    
    # Element {http://subsonic.org/restapi}chatMessages uses Python identifier chatMessages
    __chatMessages = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'chatMessages'), 'chatMessages', '__httpsubsonic_orgrestapi_Response_httpsubsonic_orgrestapichatMessages', False, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 34, 12), )

    
    chatMessages = property(__chatMessages.value, __chatMessages.set, None, None)

    
    # Element {http://subsonic.org/restapi}albumList uses Python identifier albumList
    __albumList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'albumList'), 'albumList', '__httpsubsonic_orgrestapi_Response_httpsubsonic_orgrestapialbumList', False, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 35, 12), )

    
    albumList = property(__albumList.value, __albumList.set, None, None)

    
    # Element {http://subsonic.org/restapi}albumList2 uses Python identifier albumList2
    __albumList2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'albumList2'), 'albumList2', '__httpsubsonic_orgrestapi_Response_httpsubsonic_orgrestapialbumList2', False, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 36, 12), )

    
    albumList2 = property(__albumList2.value, __albumList2.set, None, None)

    
    # Element {http://subsonic.org/restapi}randomSongs uses Python identifier randomSongs
    __randomSongs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'randomSongs'), 'randomSongs', '__httpsubsonic_orgrestapi_Response_httpsubsonic_orgrestapirandomSongs', False, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 37, 12), )

    
    randomSongs = property(__randomSongs.value, __randomSongs.set, None, None)

    
    # Element {http://subsonic.org/restapi}songsByGenre uses Python identifier songsByGenre
    __songsByGenre = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'songsByGenre'), 'songsByGenre', '__httpsubsonic_orgrestapi_Response_httpsubsonic_orgrestapisongsByGenre', False, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 38, 12), )

    
    songsByGenre = property(__songsByGenre.value, __songsByGenre.set, None, None)

    
    # Element {http://subsonic.org/restapi}lyrics uses Python identifier lyrics
    __lyrics = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lyrics'), 'lyrics', '__httpsubsonic_orgrestapi_Response_httpsubsonic_orgrestapilyrics', False, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 39, 12), )

    
    lyrics = property(__lyrics.value, __lyrics.set, None, None)

    
    # Element {http://subsonic.org/restapi}podcasts uses Python identifier podcasts
    __podcasts = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'podcasts'), 'podcasts', '__httpsubsonic_orgrestapi_Response_httpsubsonic_orgrestapipodcasts', False, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 40, 12), )

    
    podcasts = property(__podcasts.value, __podcasts.set, None, None)

    
    # Element {http://subsonic.org/restapi}newestPodcasts uses Python identifier newestPodcasts
    __newestPodcasts = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'newestPodcasts'), 'newestPodcasts', '__httpsubsonic_orgrestapi_Response_httpsubsonic_orgrestapinewestPodcasts', False, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 41, 12), )

    
    newestPodcasts = property(__newestPodcasts.value, __newestPodcasts.set, None, None)

    
    # Element {http://subsonic.org/restapi}internetRadioStations uses Python identifier internetRadioStations
    __internetRadioStations = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'internetRadioStations'), 'internetRadioStations', '__httpsubsonic_orgrestapi_Response_httpsubsonic_orgrestapiinternetRadioStations', False, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 42, 12), )

    
    internetRadioStations = property(__internetRadioStations.value, __internetRadioStations.set, None, None)

    
    # Element {http://subsonic.org/restapi}bookmarks uses Python identifier bookmarks
    __bookmarks = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'bookmarks'), 'bookmarks', '__httpsubsonic_orgrestapi_Response_httpsubsonic_orgrestapibookmarks', False, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 43, 12), )

    
    bookmarks = property(__bookmarks.value, __bookmarks.set, None, None)

    
    # Element {http://subsonic.org/restapi}playQueue uses Python identifier playQueue
    __playQueue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'playQueue'), 'playQueue', '__httpsubsonic_orgrestapi_Response_httpsubsonic_orgrestapiplayQueue', False, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 44, 12), )

    
    playQueue = property(__playQueue.value, __playQueue.set, None, None)

    
    # Element {http://subsonic.org/restapi}shares uses Python identifier shares
    __shares = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'shares'), 'shares', '__httpsubsonic_orgrestapi_Response_httpsubsonic_orgrestapishares', False, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 45, 12), )

    
    shares = property(__shares.value, __shares.set, None, None)

    
    # Element {http://subsonic.org/restapi}starred uses Python identifier starred
    __starred = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'starred'), 'starred', '__httpsubsonic_orgrestapi_Response_httpsubsonic_orgrestapistarred', False, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 46, 12), )

    
    starred = property(__starred.value, __starred.set, None, None)

    
    # Element {http://subsonic.org/restapi}starred2 uses Python identifier starred2
    __starred2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'starred2'), 'starred2', '__httpsubsonic_orgrestapi_Response_httpsubsonic_orgrestapistarred2', False, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 47, 12), )

    
    starred2 = property(__starred2.value, __starred2.set, None, None)

    
    # Element {http://subsonic.org/restapi}albumInfo uses Python identifier albumInfo
    __albumInfo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'albumInfo'), 'albumInfo', '__httpsubsonic_orgrestapi_Response_httpsubsonic_orgrestapialbumInfo', False, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 48, 12), )

    
    albumInfo = property(__albumInfo.value, __albumInfo.set, None, None)

    
    # Element {http://subsonic.org/restapi}artistInfo uses Python identifier artistInfo
    __artistInfo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'artistInfo'), 'artistInfo', '__httpsubsonic_orgrestapi_Response_httpsubsonic_orgrestapiartistInfo', False, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 49, 12), )

    
    artistInfo = property(__artistInfo.value, __artistInfo.set, None, None)

    
    # Element {http://subsonic.org/restapi}artistInfo2 uses Python identifier artistInfo2
    __artistInfo2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'artistInfo2'), 'artistInfo2', '__httpsubsonic_orgrestapi_Response_httpsubsonic_orgrestapiartistInfo2', False, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 50, 12), )

    
    artistInfo2 = property(__artistInfo2.value, __artistInfo2.set, None, None)

    
    # Element {http://subsonic.org/restapi}similarSongs uses Python identifier similarSongs
    __similarSongs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'similarSongs'), 'similarSongs', '__httpsubsonic_orgrestapi_Response_httpsubsonic_orgrestapisimilarSongs', False, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 51, 12), )

    
    similarSongs = property(__similarSongs.value, __similarSongs.set, None, None)

    
    # Element {http://subsonic.org/restapi}similarSongs2 uses Python identifier similarSongs2
    __similarSongs2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'similarSongs2'), 'similarSongs2', '__httpsubsonic_orgrestapi_Response_httpsubsonic_orgrestapisimilarSongs2', False, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 52, 12), )

    
    similarSongs2 = property(__similarSongs2.value, __similarSongs2.set, None, None)

    
    # Element {http://subsonic.org/restapi}topSongs uses Python identifier topSongs
    __topSongs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'topSongs'), 'topSongs', '__httpsubsonic_orgrestapi_Response_httpsubsonic_orgrestapitopSongs', False, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 53, 12), )

    
    topSongs = property(__topSongs.value, __topSongs.set, None, None)

    
    # Element {http://subsonic.org/restapi}error uses Python identifier error
    __error = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'error'), 'error', '__httpsubsonic_orgrestapi_Response_httpsubsonic_orgrestapierror', False, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 54, 12), )

    
    error = property(__error.value, __error.set, None, None)

    
    # Attribute status uses Python identifier status
    __status = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'status'), 'status', '__httpsubsonic_orgrestapi_Response_status', _module_typeBindings.ResponseStatus, required=True)
    __status._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 56, 8)
    __status._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 56, 8)
    
    status = property(__status.value, __status.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__httpsubsonic_orgrestapi_Response_version', _module_typeBindings.Version, required=True)
    __version._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 57, 8)
    __version._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 57, 8)
    
    version = property(__version.value, __version.set, None, None)

    _ElementMap.update({
        __musicFolders.name() : __musicFolders,
        __indexes.name() : __indexes,
        __directory.name() : __directory,
        __genres.name() : __genres,
        __artists.name() : __artists,
        __artist.name() : __artist,
        __album.name() : __album,
        __song.name() : __song,
        __videos.name() : __videos,
        __videoInfo.name() : __videoInfo,
        __nowPlaying.name() : __nowPlaying,
        __searchResult.name() : __searchResult,
        __searchResult2.name() : __searchResult2,
        __searchResult3.name() : __searchResult3,
        __playlists.name() : __playlists,
        __playlist.name() : __playlist,
        __jukeboxStatus.name() : __jukeboxStatus,
        __jukeboxPlaylist.name() : __jukeboxPlaylist,
        __license.name() : __license,
        __users.name() : __users,
        __user.name() : __user,
        __chatMessages.name() : __chatMessages,
        __albumList.name() : __albumList,
        __albumList2.name() : __albumList2,
        __randomSongs.name() : __randomSongs,
        __songsByGenre.name() : __songsByGenre,
        __lyrics.name() : __lyrics,
        __podcasts.name() : __podcasts,
        __newestPodcasts.name() : __newestPodcasts,
        __internetRadioStations.name() : __internetRadioStations,
        __bookmarks.name() : __bookmarks,
        __playQueue.name() : __playQueue,
        __shares.name() : __shares,
        __starred.name() : __starred,
        __starred2.name() : __starred2,
        __albumInfo.name() : __albumInfo,
        __artistInfo.name() : __artistInfo,
        __artistInfo2.name() : __artistInfo2,
        __similarSongs.name() : __similarSongs,
        __similarSongs2.name() : __similarSongs2,
        __topSongs.name() : __topSongs,
        __error.name() : __error
    })
    _AttributeMap.update({
        __status.name() : __status,
        __version.name() : __version
    })
_module_typeBindings.Response = Response
Namespace.addCategoryObject('typeBinding', 'Response', Response)


# Complex type {http://subsonic.org/restapi}Artist with content type EMPTY
class Artist (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://subsonic.org/restapi}Artist with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Artist')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 101, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpsubsonic_orgrestapi_Artist_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 102, 8)
    __id._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 102, 8)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpsubsonic_orgrestapi_Artist_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 103, 8)
    __name._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 103, 8)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute starred uses Python identifier starred
    __starred = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'starred'), 'starred', '__httpsubsonic_orgrestapi_Artist_starred', pyxb.binding.datatypes.dateTime)
    __starred._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 104, 8)
    __starred._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 104, 8)
    
    starred = property(__starred.value, __starred.set, None, None)

    
    # Attribute userRating uses Python identifier userRating
    __userRating = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'userRating'), 'userRating', '__httpsubsonic_orgrestapi_Artist_userRating', _module_typeBindings.UserRating)
    __userRating._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 105, 8)
    __userRating._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 105, 8)
    
    userRating = property(__userRating.value, __userRating.set, None, None)

    
    # Attribute averageRating uses Python identifier averageRating
    __averageRating = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'averageRating'), 'averageRating', '__httpsubsonic_orgrestapi_Artist_averageRating', _module_typeBindings.AverageRating)
    __averageRating._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 106, 8)
    __averageRating._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 106, 8)
    
    averageRating = property(__averageRating.value, __averageRating.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __name.name() : __name,
        __starred.name() : __starred,
        __userRating.name() : __userRating,
        __averageRating.name() : __averageRating
    })
_module_typeBindings.Artist = Artist
Namespace.addCategoryObject('typeBinding', 'Artist', Artist)


# Complex type {http://subsonic.org/restapi}ArtistWithAlbumsID3 with content type ELEMENT_ONLY
class ArtistWithAlbumsID3 (ArtistID3):
    """Complex type {http://subsonic.org/restapi}ArtistWithAlbumsID3 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ArtistWithAlbumsID3')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 142, 4)
    _ElementMap = ArtistID3._ElementMap.copy()
    _AttributeMap = ArtistID3._AttributeMap.copy()
    # Base type is ArtistID3
    
    # Element {http://subsonic.org/restapi}album uses Python identifier album
    __album = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'album'), 'album', '__httpsubsonic_orgrestapi_ArtistWithAlbumsID3_httpsubsonic_orgrestapialbum', True, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 146, 20), )

    
    album = property(__album.value, __album.set, None, None)

    
    # Attribute id inherited from {http://subsonic.org/restapi}ArtistID3
    
    # Attribute name inherited from {http://subsonic.org/restapi}ArtistID3
    
    # Attribute coverArt inherited from {http://subsonic.org/restapi}ArtistID3
    
    # Attribute albumCount inherited from {http://subsonic.org/restapi}ArtistID3
    
    # Attribute starred inherited from {http://subsonic.org/restapi}ArtistID3
    _ElementMap.update({
        __album.name() : __album
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ArtistWithAlbumsID3 = ArtistWithAlbumsID3
Namespace.addCategoryObject('typeBinding', 'ArtistWithAlbumsID3', ArtistWithAlbumsID3)


# Complex type {http://subsonic.org/restapi}AlbumWithSongsID3 with content type ELEMENT_ONLY
class AlbumWithSongsID3 (AlbumID3):
    """Complex type {http://subsonic.org/restapi}AlbumWithSongsID3 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AlbumWithSongsID3')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 167, 4)
    _ElementMap = AlbumID3._ElementMap.copy()
    _AttributeMap = AlbumID3._AttributeMap.copy()
    # Base type is AlbumID3
    
    # Element {http://subsonic.org/restapi}song uses Python identifier song
    __song = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'song'), 'song', '__httpsubsonic_orgrestapi_AlbumWithSongsID3_httpsubsonic_orgrestapisong', True, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 171, 20), )

    
    song = property(__song.value, __song.set, None, None)

    
    # Attribute id inherited from {http://subsonic.org/restapi}AlbumID3
    
    # Attribute name inherited from {http://subsonic.org/restapi}AlbumID3
    
    # Attribute artist inherited from {http://subsonic.org/restapi}AlbumID3
    
    # Attribute artistId inherited from {http://subsonic.org/restapi}AlbumID3
    
    # Attribute coverArt inherited from {http://subsonic.org/restapi}AlbumID3
    
    # Attribute songCount inherited from {http://subsonic.org/restapi}AlbumID3
    
    # Attribute duration inherited from {http://subsonic.org/restapi}AlbumID3
    
    # Attribute playCount inherited from {http://subsonic.org/restapi}AlbumID3
    
    # Attribute created inherited from {http://subsonic.org/restapi}AlbumID3
    
    # Attribute starred inherited from {http://subsonic.org/restapi}AlbumID3
    
    # Attribute year inherited from {http://subsonic.org/restapi}AlbumID3
    
    # Attribute genre inherited from {http://subsonic.org/restapi}AlbumID3
    _ElementMap.update({
        __song.name() : __song
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AlbumWithSongsID3 = AlbumWithSongsID3
Namespace.addCategoryObject('typeBinding', 'AlbumWithSongsID3', AlbumWithSongsID3)


# Complex type {http://subsonic.org/restapi}Directory with content type ELEMENT_ONLY
class Directory (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://subsonic.org/restapi}Directory with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Directory')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 209, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://subsonic.org/restapi}child uses Python identifier child
    __child = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'child'), 'child', '__httpsubsonic_orgrestapi_Directory_httpsubsonic_orgrestapichild', True, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 211, 12), )

    
    child = property(__child.value, __child.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpsubsonic_orgrestapi_Directory_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 213, 8)
    __id._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 213, 8)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute parent uses Python identifier parent
    __parent = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'parent'), 'parent', '__httpsubsonic_orgrestapi_Directory_parent', pyxb.binding.datatypes.string)
    __parent._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 214, 8)
    __parent._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 214, 8)
    
    parent = property(__parent.value, __parent.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpsubsonic_orgrestapi_Directory_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 215, 8)
    __name._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 215, 8)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute starred uses Python identifier starred
    __starred = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'starred'), 'starred', '__httpsubsonic_orgrestapi_Directory_starred', pyxb.binding.datatypes.dateTime)
    __starred._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 216, 8)
    __starred._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 216, 8)
    
    starred = property(__starred.value, __starred.set, None, None)

    
    # Attribute userRating uses Python identifier userRating
    __userRating = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'userRating'), 'userRating', '__httpsubsonic_orgrestapi_Directory_userRating', _module_typeBindings.UserRating)
    __userRating._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 217, 8)
    __userRating._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 217, 8)
    
    userRating = property(__userRating.value, __userRating.set, None, None)

    
    # Attribute averageRating uses Python identifier averageRating
    __averageRating = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'averageRating'), 'averageRating', '__httpsubsonic_orgrestapi_Directory_averageRating', _module_typeBindings.AverageRating)
    __averageRating._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 218, 8)
    __averageRating._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 218, 8)
    
    averageRating = property(__averageRating.value, __averageRating.set, None, None)

    
    # Attribute playCount uses Python identifier playCount
    __playCount = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'playCount'), 'playCount', '__httpsubsonic_orgrestapi_Directory_playCount', pyxb.binding.datatypes.long)
    __playCount._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 219, 8)
    __playCount._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 219, 8)
    
    playCount = property(__playCount.value, __playCount.set, None, None)

    _ElementMap.update({
        __child.name() : __child
    })
    _AttributeMap.update({
        __id.name() : __id,
        __parent.name() : __parent,
        __name.name() : __name,
        __starred.name() : __starred,
        __userRating.name() : __userRating,
        __averageRating.name() : __averageRating,
        __playCount.name() : __playCount
    })
_module_typeBindings.Directory = Directory
Namespace.addCategoryObject('typeBinding', 'Directory', Directory)


# Complex type {http://subsonic.org/restapi}Child with content type EMPTY
class Child (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://subsonic.org/restapi}Child with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Child')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 222, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpsubsonic_orgrestapi_Child_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 223, 8)
    __id._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 223, 8)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute parent uses Python identifier parent
    __parent = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'parent'), 'parent', '__httpsubsonic_orgrestapi_Child_parent', pyxb.binding.datatypes.string)
    __parent._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 224, 8)
    __parent._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 224, 8)
    
    parent = property(__parent.value, __parent.set, None, None)

    
    # Attribute isDir uses Python identifier isDir
    __isDir = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'isDir'), 'isDir', '__httpsubsonic_orgrestapi_Child_isDir', pyxb.binding.datatypes.boolean, required=True)
    __isDir._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 225, 8)
    __isDir._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 225, 8)
    
    isDir = property(__isDir.value, __isDir.set, None, None)

    
    # Attribute title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'title'), 'title', '__httpsubsonic_orgrestapi_Child_title', pyxb.binding.datatypes.string, required=True)
    __title._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 226, 8)
    __title._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 226, 8)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute album uses Python identifier album
    __album = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'album'), 'album', '__httpsubsonic_orgrestapi_Child_album', pyxb.binding.datatypes.string)
    __album._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 227, 8)
    __album._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 227, 8)
    
    album = property(__album.value, __album.set, None, None)

    
    # Attribute artist uses Python identifier artist
    __artist = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'artist'), 'artist', '__httpsubsonic_orgrestapi_Child_artist', pyxb.binding.datatypes.string)
    __artist._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 228, 8)
    __artist._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 228, 8)
    
    artist = property(__artist.value, __artist.set, None, None)

    
    # Attribute track uses Python identifier track
    __track = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'track'), 'track', '__httpsubsonic_orgrestapi_Child_track', pyxb.binding.datatypes.int)
    __track._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 229, 8)
    __track._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 229, 8)
    
    track = property(__track.value, __track.set, None, None)

    
    # Attribute year uses Python identifier year
    __year = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'year'), 'year', '__httpsubsonic_orgrestapi_Child_year', pyxb.binding.datatypes.int)
    __year._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 230, 8)
    __year._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 230, 8)
    
    year = property(__year.value, __year.set, None, None)

    
    # Attribute genre uses Python identifier genre
    __genre = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'genre'), 'genre', '__httpsubsonic_orgrestapi_Child_genre', pyxb.binding.datatypes.string)
    __genre._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 231, 8)
    __genre._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 231, 8)
    
    genre = property(__genre.value, __genre.set, None, None)

    
    # Attribute coverArt uses Python identifier coverArt
    __coverArt = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'coverArt'), 'coverArt', '__httpsubsonic_orgrestapi_Child_coverArt', pyxb.binding.datatypes.string)
    __coverArt._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 232, 8)
    __coverArt._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 232, 8)
    
    coverArt = property(__coverArt.value, __coverArt.set, None, None)

    
    # Attribute size uses Python identifier size
    __size = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'size'), 'size', '__httpsubsonic_orgrestapi_Child_size', pyxb.binding.datatypes.long)
    __size._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 233, 8)
    __size._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 233, 8)
    
    size = property(__size.value, __size.set, None, None)

    
    # Attribute contentType uses Python identifier contentType
    __contentType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'contentType'), 'contentType', '__httpsubsonic_orgrestapi_Child_contentType', pyxb.binding.datatypes.string)
    __contentType._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 234, 8)
    __contentType._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 234, 8)
    
    contentType = property(__contentType.value, __contentType.set, None, None)

    
    # Attribute suffix uses Python identifier suffix
    __suffix = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'suffix'), 'suffix', '__httpsubsonic_orgrestapi_Child_suffix', pyxb.binding.datatypes.string)
    __suffix._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 235, 8)
    __suffix._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 235, 8)
    
    suffix = property(__suffix.value, __suffix.set, None, None)

    
    # Attribute transcodedContentType uses Python identifier transcodedContentType
    __transcodedContentType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'transcodedContentType'), 'transcodedContentType', '__httpsubsonic_orgrestapi_Child_transcodedContentType', pyxb.binding.datatypes.string)
    __transcodedContentType._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 236, 8)
    __transcodedContentType._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 236, 8)
    
    transcodedContentType = property(__transcodedContentType.value, __transcodedContentType.set, None, None)

    
    # Attribute transcodedSuffix uses Python identifier transcodedSuffix
    __transcodedSuffix = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'transcodedSuffix'), 'transcodedSuffix', '__httpsubsonic_orgrestapi_Child_transcodedSuffix', pyxb.binding.datatypes.string)
    __transcodedSuffix._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 237, 8)
    __transcodedSuffix._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 237, 8)
    
    transcodedSuffix = property(__transcodedSuffix.value, __transcodedSuffix.set, None, None)

    
    # Attribute duration uses Python identifier duration
    __duration = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'duration'), 'duration', '__httpsubsonic_orgrestapi_Child_duration', pyxb.binding.datatypes.int)
    __duration._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 238, 8)
    __duration._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 238, 8)
    
    duration = property(__duration.value, __duration.set, None, None)

    
    # Attribute bitRate uses Python identifier bitRate
    __bitRate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'bitRate'), 'bitRate', '__httpsubsonic_orgrestapi_Child_bitRate', pyxb.binding.datatypes.int)
    __bitRate._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 239, 8)
    __bitRate._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 239, 8)
    
    bitRate = property(__bitRate.value, __bitRate.set, None, None)

    
    # Attribute path uses Python identifier path
    __path = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'path'), 'path', '__httpsubsonic_orgrestapi_Child_path', pyxb.binding.datatypes.string)
    __path._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 240, 8)
    __path._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 240, 8)
    
    path = property(__path.value, __path.set, None, None)

    
    # Attribute isVideo uses Python identifier isVideo
    __isVideo = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'isVideo'), 'isVideo', '__httpsubsonic_orgrestapi_Child_isVideo', pyxb.binding.datatypes.boolean)
    __isVideo._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 241, 8)
    __isVideo._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 241, 8)
    
    isVideo = property(__isVideo.value, __isVideo.set, None, None)

    
    # Attribute userRating uses Python identifier userRating
    __userRating = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'userRating'), 'userRating', '__httpsubsonic_orgrestapi_Child_userRating', _module_typeBindings.UserRating)
    __userRating._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 242, 8)
    __userRating._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 242, 8)
    
    userRating = property(__userRating.value, __userRating.set, None, None)

    
    # Attribute averageRating uses Python identifier averageRating
    __averageRating = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'averageRating'), 'averageRating', '__httpsubsonic_orgrestapi_Child_averageRating', _module_typeBindings.AverageRating)
    __averageRating._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 243, 8)
    __averageRating._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 243, 8)
    
    averageRating = property(__averageRating.value, __averageRating.set, None, None)

    
    # Attribute playCount uses Python identifier playCount
    __playCount = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'playCount'), 'playCount', '__httpsubsonic_orgrestapi_Child_playCount', pyxb.binding.datatypes.long)
    __playCount._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 244, 8)
    __playCount._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 244, 8)
    
    playCount = property(__playCount.value, __playCount.set, None, None)

    
    # Attribute discNumber uses Python identifier discNumber
    __discNumber = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'discNumber'), 'discNumber', '__httpsubsonic_orgrestapi_Child_discNumber', pyxb.binding.datatypes.int)
    __discNumber._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 245, 8)
    __discNumber._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 245, 8)
    
    discNumber = property(__discNumber.value, __discNumber.set, None, None)

    
    # Attribute created uses Python identifier created
    __created = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'created'), 'created', '__httpsubsonic_orgrestapi_Child_created', pyxb.binding.datatypes.dateTime)
    __created._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 246, 8)
    __created._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 246, 8)
    
    created = property(__created.value, __created.set, None, None)

    
    # Attribute starred uses Python identifier starred
    __starred = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'starred'), 'starred', '__httpsubsonic_orgrestapi_Child_starred', pyxb.binding.datatypes.dateTime)
    __starred._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 247, 8)
    __starred._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 247, 8)
    
    starred = property(__starred.value, __starred.set, None, None)

    
    # Attribute albumId uses Python identifier albumId
    __albumId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'albumId'), 'albumId', '__httpsubsonic_orgrestapi_Child_albumId', pyxb.binding.datatypes.string)
    __albumId._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 248, 8)
    __albumId._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 248, 8)
    
    albumId = property(__albumId.value, __albumId.set, None, None)

    
    # Attribute artistId uses Python identifier artistId
    __artistId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'artistId'), 'artistId', '__httpsubsonic_orgrestapi_Child_artistId', pyxb.binding.datatypes.string)
    __artistId._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 249, 8)
    __artistId._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 249, 8)
    
    artistId = property(__artistId.value, __artistId.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__httpsubsonic_orgrestapi_Child_type', _module_typeBindings.MediaType)
    __type._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 250, 8)
    __type._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 250, 8)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute bookmarkPosition uses Python identifier bookmarkPosition
    __bookmarkPosition = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'bookmarkPosition'), 'bookmarkPosition', '__httpsubsonic_orgrestapi_Child_bookmarkPosition', pyxb.binding.datatypes.long)
    __bookmarkPosition._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 251, 8)
    __bookmarkPosition._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 251, 8)
    
    bookmarkPosition = property(__bookmarkPosition.value, __bookmarkPosition.set, None, None)

    
    # Attribute originalWidth uses Python identifier originalWidth
    __originalWidth = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'originalWidth'), 'originalWidth', '__httpsubsonic_orgrestapi_Child_originalWidth', pyxb.binding.datatypes.int)
    __originalWidth._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 252, 8)
    __originalWidth._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 252, 8)
    
    originalWidth = property(__originalWidth.value, __originalWidth.set, None, None)

    
    # Attribute originalHeight uses Python identifier originalHeight
    __originalHeight = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'originalHeight'), 'originalHeight', '__httpsubsonic_orgrestapi_Child_originalHeight', pyxb.binding.datatypes.int)
    __originalHeight._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 253, 8)
    __originalHeight._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 253, 8)
    
    originalHeight = property(__originalHeight.value, __originalHeight.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __parent.name() : __parent,
        __isDir.name() : __isDir,
        __title.name() : __title,
        __album.name() : __album,
        __artist.name() : __artist,
        __track.name() : __track,
        __year.name() : __year,
        __genre.name() : __genre,
        __coverArt.name() : __coverArt,
        __size.name() : __size,
        __contentType.name() : __contentType,
        __suffix.name() : __suffix,
        __transcodedContentType.name() : __transcodedContentType,
        __transcodedSuffix.name() : __transcodedSuffix,
        __duration.name() : __duration,
        __bitRate.name() : __bitRate,
        __path.name() : __path,
        __isVideo.name() : __isVideo,
        __userRating.name() : __userRating,
        __averageRating.name() : __averageRating,
        __playCount.name() : __playCount,
        __discNumber.name() : __discNumber,
        __created.name() : __created,
        __starred.name() : __starred,
        __albumId.name() : __albumId,
        __artistId.name() : __artistId,
        __type.name() : __type,
        __bookmarkPosition.name() : __bookmarkPosition,
        __originalWidth.name() : __originalWidth,
        __originalHeight.name() : __originalHeight
    })
_module_typeBindings.Child = Child
Namespace.addCategoryObject('typeBinding', 'Child', Child)


# Complex type {http://subsonic.org/restapi}PlaylistWithSongs with content type ELEMENT_ONLY
class PlaylistWithSongs (Playlist):
    """Complex type {http://subsonic.org/restapi}PlaylistWithSongs with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PlaylistWithSongs')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 343, 4)
    _ElementMap = Playlist._ElementMap.copy()
    _AttributeMap = Playlist._AttributeMap.copy()
    # Base type is Playlist
    
    # Element allowedUser ({http://subsonic.org/restapi}allowedUser) inherited from {http://subsonic.org/restapi}Playlist
    
    # Element {http://subsonic.org/restapi}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'entry'), 'entry', '__httpsubsonic_orgrestapi_PlaylistWithSongs_httpsubsonic_orgrestapientry', True, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 347, 20), )

    
    entry = property(__entry.value, __entry.set, None, None)

    
    # Attribute id inherited from {http://subsonic.org/restapi}Playlist
    
    # Attribute name inherited from {http://subsonic.org/restapi}Playlist
    
    # Attribute comment inherited from {http://subsonic.org/restapi}Playlist
    
    # Attribute owner inherited from {http://subsonic.org/restapi}Playlist
    
    # Attribute public inherited from {http://subsonic.org/restapi}Playlist
    
    # Attribute songCount inherited from {http://subsonic.org/restapi}Playlist
    
    # Attribute duration inherited from {http://subsonic.org/restapi}Playlist
    
    # Attribute created inherited from {http://subsonic.org/restapi}Playlist
    
    # Attribute changed inherited from {http://subsonic.org/restapi}Playlist
    
    # Attribute coverArt inherited from {http://subsonic.org/restapi}Playlist
    _ElementMap.update({
        __entry.name() : __entry
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PlaylistWithSongs = PlaylistWithSongs
Namespace.addCategoryObject('typeBinding', 'PlaylistWithSongs', PlaylistWithSongs)


# Complex type {http://subsonic.org/restapi}JukeboxPlaylist with content type ELEMENT_ONLY
class JukeboxPlaylist (JukeboxStatus):
    """Complex type {http://subsonic.org/restapi}JukeboxPlaylist with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'JukeboxPlaylist')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 360, 4)
    _ElementMap = JukeboxStatus._ElementMap.copy()
    _AttributeMap = JukeboxStatus._AttributeMap.copy()
    # Base type is JukeboxStatus
    
    # Element {http://subsonic.org/restapi}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'entry'), 'entry', '__httpsubsonic_orgrestapi_JukeboxPlaylist_httpsubsonic_orgrestapientry', True, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 364, 20), )

    
    entry = property(__entry.value, __entry.set, None, None)

    
    # Attribute currentIndex inherited from {http://subsonic.org/restapi}JukeboxStatus
    
    # Attribute playing inherited from {http://subsonic.org/restapi}JukeboxStatus
    
    # Attribute gain inherited from {http://subsonic.org/restapi}JukeboxStatus
    
    # Attribute position inherited from {http://subsonic.org/restapi}JukeboxStatus
    _ElementMap.update({
        __entry.name() : __entry
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.JukeboxPlaylist = JukeboxPlaylist
Namespace.addCategoryObject('typeBinding', 'JukeboxPlaylist', JukeboxPlaylist)


# Complex type {http://subsonic.org/restapi}PodcastChannel with content type ELEMENT_ONLY
class PodcastChannel (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://subsonic.org/restapi}PodcastChannel with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PodcastChannel')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 411, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://subsonic.org/restapi}episode uses Python identifier episode
    __episode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'episode'), 'episode', '__httpsubsonic_orgrestapi_PodcastChannel_httpsubsonic_orgrestapiepisode', True, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 413, 12), )

    
    episode = property(__episode.value, __episode.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpsubsonic_orgrestapi_PodcastChannel_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 415, 8)
    __id._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 415, 8)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute url uses Python identifier url
    __url = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'url'), 'url', '__httpsubsonic_orgrestapi_PodcastChannel_url', pyxb.binding.datatypes.string, required=True)
    __url._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 416, 8)
    __url._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 416, 8)
    
    url = property(__url.value, __url.set, None, None)

    
    # Attribute title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'title'), 'title', '__httpsubsonic_orgrestapi_PodcastChannel_title', pyxb.binding.datatypes.string)
    __title._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 417, 8)
    __title._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 417, 8)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute description uses Python identifier description
    __description = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'description'), 'description', '__httpsubsonic_orgrestapi_PodcastChannel_description', pyxb.binding.datatypes.string)
    __description._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 418, 8)
    __description._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 418, 8)
    
    description = property(__description.value, __description.set, None, None)

    
    # Attribute coverArt uses Python identifier coverArt
    __coverArt = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'coverArt'), 'coverArt', '__httpsubsonic_orgrestapi_PodcastChannel_coverArt', pyxb.binding.datatypes.string)
    __coverArt._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 419, 8)
    __coverArt._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 419, 8)
    
    coverArt = property(__coverArt.value, __coverArt.set, None, None)

    
    # Attribute originalImageUrl uses Python identifier originalImageUrl
    __originalImageUrl = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'originalImageUrl'), 'originalImageUrl', '__httpsubsonic_orgrestapi_PodcastChannel_originalImageUrl', pyxb.binding.datatypes.string)
    __originalImageUrl._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 420, 8)
    __originalImageUrl._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 420, 8)
    
    originalImageUrl = property(__originalImageUrl.value, __originalImageUrl.set, None, None)

    
    # Attribute status uses Python identifier status
    __status = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'status'), 'status', '__httpsubsonic_orgrestapi_PodcastChannel_status', _module_typeBindings.PodcastStatus, required=True)
    __status._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 421, 8)
    __status._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 421, 8)
    
    status = property(__status.value, __status.set, None, None)

    
    # Attribute errorMessage uses Python identifier errorMessage
    __errorMessage = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'errorMessage'), 'errorMessage', '__httpsubsonic_orgrestapi_PodcastChannel_errorMessage', pyxb.binding.datatypes.string)
    __errorMessage._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 422, 8)
    __errorMessage._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 422, 8)
    
    errorMessage = property(__errorMessage.value, __errorMessage.set, None, None)

    _ElementMap.update({
        __episode.name() : __episode
    })
    _AttributeMap.update({
        __id.name() : __id,
        __url.name() : __url,
        __title.name() : __title,
        __description.name() : __description,
        __coverArt.name() : __coverArt,
        __originalImageUrl.name() : __originalImageUrl,
        __status.name() : __status,
        __errorMessage.name() : __errorMessage
    })
_module_typeBindings.PodcastChannel = PodcastChannel
Namespace.addCategoryObject('typeBinding', 'PodcastChannel', PodcastChannel)


# Complex type {http://subsonic.org/restapi}ArtistInfo with content type ELEMENT_ONLY
class ArtistInfo (ArtistInfoBase):
    """Complex type {http://subsonic.org/restapi}ArtistInfo with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ArtistInfo')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 545, 4)
    _ElementMap = ArtistInfoBase._ElementMap.copy()
    _AttributeMap = ArtistInfoBase._AttributeMap.copy()
    # Base type is ArtistInfoBase
    
    # Element biography ({http://subsonic.org/restapi}biography) inherited from {http://subsonic.org/restapi}ArtistInfoBase
    
    # Element musicBrainzId ({http://subsonic.org/restapi}musicBrainzId) inherited from {http://subsonic.org/restapi}ArtistInfoBase
    
    # Element lastFmUrl ({http://subsonic.org/restapi}lastFmUrl) inherited from {http://subsonic.org/restapi}ArtistInfoBase
    
    # Element smallImageUrl ({http://subsonic.org/restapi}smallImageUrl) inherited from {http://subsonic.org/restapi}ArtistInfoBase
    
    # Element mediumImageUrl ({http://subsonic.org/restapi}mediumImageUrl) inherited from {http://subsonic.org/restapi}ArtistInfoBase
    
    # Element largeImageUrl ({http://subsonic.org/restapi}largeImageUrl) inherited from {http://subsonic.org/restapi}ArtistInfoBase
    
    # Element {http://subsonic.org/restapi}similarArtist uses Python identifier similarArtist
    __similarArtist = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'similarArtist'), 'similarArtist', '__httpsubsonic_orgrestapi_ArtistInfo_httpsubsonic_orgrestapisimilarArtist', True, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 549, 20), )

    
    similarArtist = property(__similarArtist.value, __similarArtist.set, None, None)

    _ElementMap.update({
        __similarArtist.name() : __similarArtist
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ArtistInfo = ArtistInfo
Namespace.addCategoryObject('typeBinding', 'ArtistInfo', ArtistInfo)


# Complex type {http://subsonic.org/restapi}ArtistInfo2 with content type ELEMENT_ONLY
class ArtistInfo2 (ArtistInfoBase):
    """Complex type {http://subsonic.org/restapi}ArtistInfo2 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ArtistInfo2')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 555, 4)
    _ElementMap = ArtistInfoBase._ElementMap.copy()
    _AttributeMap = ArtistInfoBase._AttributeMap.copy()
    # Base type is ArtistInfoBase
    
    # Element biography ({http://subsonic.org/restapi}biography) inherited from {http://subsonic.org/restapi}ArtistInfoBase
    
    # Element musicBrainzId ({http://subsonic.org/restapi}musicBrainzId) inherited from {http://subsonic.org/restapi}ArtistInfoBase
    
    # Element lastFmUrl ({http://subsonic.org/restapi}lastFmUrl) inherited from {http://subsonic.org/restapi}ArtistInfoBase
    
    # Element smallImageUrl ({http://subsonic.org/restapi}smallImageUrl) inherited from {http://subsonic.org/restapi}ArtistInfoBase
    
    # Element mediumImageUrl ({http://subsonic.org/restapi}mediumImageUrl) inherited from {http://subsonic.org/restapi}ArtistInfoBase
    
    # Element largeImageUrl ({http://subsonic.org/restapi}largeImageUrl) inherited from {http://subsonic.org/restapi}ArtistInfoBase
    
    # Element {http://subsonic.org/restapi}similarArtist uses Python identifier similarArtist
    __similarArtist = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'similarArtist'), 'similarArtist', '__httpsubsonic_orgrestapi_ArtistInfo2_httpsubsonic_orgrestapisimilarArtist', True, pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 559, 20), )

    
    similarArtist = property(__similarArtist.value, __similarArtist.set, None, None)

    _ElementMap.update({
        __similarArtist.name() : __similarArtist
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ArtistInfo2 = ArtistInfo2
Namespace.addCategoryObject('typeBinding', 'ArtistInfo2', ArtistInfo2)


# Complex type {http://subsonic.org/restapi}NowPlayingEntry with content type EMPTY
class NowPlayingEntry (Child):
    """Complex type {http://subsonic.org/restapi}NowPlayingEntry with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NowPlayingEntry')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 285, 4)
    _ElementMap = Child._ElementMap.copy()
    _AttributeMap = Child._AttributeMap.copy()
    # Base type is Child
    
    # Attribute id inherited from {http://subsonic.org/restapi}Child
    
    # Attribute parent inherited from {http://subsonic.org/restapi}Child
    
    # Attribute isDir inherited from {http://subsonic.org/restapi}Child
    
    # Attribute title inherited from {http://subsonic.org/restapi}Child
    
    # Attribute album inherited from {http://subsonic.org/restapi}Child
    
    # Attribute artist inherited from {http://subsonic.org/restapi}Child
    
    # Attribute track inherited from {http://subsonic.org/restapi}Child
    
    # Attribute year inherited from {http://subsonic.org/restapi}Child
    
    # Attribute genre inherited from {http://subsonic.org/restapi}Child
    
    # Attribute coverArt inherited from {http://subsonic.org/restapi}Child
    
    # Attribute size inherited from {http://subsonic.org/restapi}Child
    
    # Attribute contentType inherited from {http://subsonic.org/restapi}Child
    
    # Attribute suffix inherited from {http://subsonic.org/restapi}Child
    
    # Attribute transcodedContentType inherited from {http://subsonic.org/restapi}Child
    
    # Attribute transcodedSuffix inherited from {http://subsonic.org/restapi}Child
    
    # Attribute duration inherited from {http://subsonic.org/restapi}Child
    
    # Attribute bitRate inherited from {http://subsonic.org/restapi}Child
    
    # Attribute path inherited from {http://subsonic.org/restapi}Child
    
    # Attribute isVideo inherited from {http://subsonic.org/restapi}Child
    
    # Attribute userRating inherited from {http://subsonic.org/restapi}Child
    
    # Attribute averageRating inherited from {http://subsonic.org/restapi}Child
    
    # Attribute playCount inherited from {http://subsonic.org/restapi}Child
    
    # Attribute discNumber inherited from {http://subsonic.org/restapi}Child
    
    # Attribute created inherited from {http://subsonic.org/restapi}Child
    
    # Attribute starred inherited from {http://subsonic.org/restapi}Child
    
    # Attribute albumId inherited from {http://subsonic.org/restapi}Child
    
    # Attribute artistId inherited from {http://subsonic.org/restapi}Child
    
    # Attribute type inherited from {http://subsonic.org/restapi}Child
    
    # Attribute bookmarkPosition inherited from {http://subsonic.org/restapi}Child
    
    # Attribute originalWidth inherited from {http://subsonic.org/restapi}Child
    
    # Attribute originalHeight inherited from {http://subsonic.org/restapi}Child
    
    # Attribute username uses Python identifier username
    __username = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'username'), 'username', '__httpsubsonic_orgrestapi_NowPlayingEntry_username', pyxb.binding.datatypes.string, required=True)
    __username._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 288, 16)
    __username._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 288, 16)
    
    username = property(__username.value, __username.set, None, None)

    
    # Attribute minutesAgo uses Python identifier minutesAgo
    __minutesAgo = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'minutesAgo'), 'minutesAgo', '__httpsubsonic_orgrestapi_NowPlayingEntry_minutesAgo', pyxb.binding.datatypes.int, required=True)
    __minutesAgo._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 289, 16)
    __minutesAgo._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 289, 16)
    
    minutesAgo = property(__minutesAgo.value, __minutesAgo.set, None, None)

    
    # Attribute playerId uses Python identifier playerId
    __playerId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'playerId'), 'playerId', '__httpsubsonic_orgrestapi_NowPlayingEntry_playerId', pyxb.binding.datatypes.int, required=True)
    __playerId._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 290, 16)
    __playerId._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 290, 16)
    
    playerId = property(__playerId.value, __playerId.set, None, None)

    
    # Attribute playerName uses Python identifier playerName
    __playerName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'playerName'), 'playerName', '__httpsubsonic_orgrestapi_NowPlayingEntry_playerName', pyxb.binding.datatypes.string)
    __playerName._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 291, 16)
    __playerName._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 291, 16)
    
    playerName = property(__playerName.value, __playerName.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __username.name() : __username,
        __minutesAgo.name() : __minutesAgo,
        __playerId.name() : __playerId,
        __playerName.name() : __playerName
    })
_module_typeBindings.NowPlayingEntry = NowPlayingEntry
Namespace.addCategoryObject('typeBinding', 'NowPlayingEntry', NowPlayingEntry)


# Complex type {http://subsonic.org/restapi}PodcastEpisode with content type EMPTY
class PodcastEpisode (Child):
    """Complex type {http://subsonic.org/restapi}PodcastEpisode with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PodcastEpisode')
    _XSDLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 431, 4)
    _ElementMap = Child._ElementMap.copy()
    _AttributeMap = Child._AttributeMap.copy()
    # Base type is Child
    
    # Attribute id inherited from {http://subsonic.org/restapi}Child
    
    # Attribute parent inherited from {http://subsonic.org/restapi}Child
    
    # Attribute isDir inherited from {http://subsonic.org/restapi}Child
    
    # Attribute title inherited from {http://subsonic.org/restapi}Child
    
    # Attribute album inherited from {http://subsonic.org/restapi}Child
    
    # Attribute artist inherited from {http://subsonic.org/restapi}Child
    
    # Attribute track inherited from {http://subsonic.org/restapi}Child
    
    # Attribute year inherited from {http://subsonic.org/restapi}Child
    
    # Attribute genre inherited from {http://subsonic.org/restapi}Child
    
    # Attribute coverArt inherited from {http://subsonic.org/restapi}Child
    
    # Attribute size inherited from {http://subsonic.org/restapi}Child
    
    # Attribute contentType inherited from {http://subsonic.org/restapi}Child
    
    # Attribute suffix inherited from {http://subsonic.org/restapi}Child
    
    # Attribute transcodedContentType inherited from {http://subsonic.org/restapi}Child
    
    # Attribute transcodedSuffix inherited from {http://subsonic.org/restapi}Child
    
    # Attribute duration inherited from {http://subsonic.org/restapi}Child
    
    # Attribute bitRate inherited from {http://subsonic.org/restapi}Child
    
    # Attribute path inherited from {http://subsonic.org/restapi}Child
    
    # Attribute isVideo inherited from {http://subsonic.org/restapi}Child
    
    # Attribute userRating inherited from {http://subsonic.org/restapi}Child
    
    # Attribute averageRating inherited from {http://subsonic.org/restapi}Child
    
    # Attribute playCount inherited from {http://subsonic.org/restapi}Child
    
    # Attribute discNumber inherited from {http://subsonic.org/restapi}Child
    
    # Attribute created inherited from {http://subsonic.org/restapi}Child
    
    # Attribute starred inherited from {http://subsonic.org/restapi}Child
    
    # Attribute albumId inherited from {http://subsonic.org/restapi}Child
    
    # Attribute artistId inherited from {http://subsonic.org/restapi}Child
    
    # Attribute type inherited from {http://subsonic.org/restapi}Child
    
    # Attribute bookmarkPosition inherited from {http://subsonic.org/restapi}Child
    
    # Attribute originalWidth inherited from {http://subsonic.org/restapi}Child
    
    # Attribute originalHeight inherited from {http://subsonic.org/restapi}Child
    
    # Attribute streamId uses Python identifier streamId
    __streamId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'streamId'), 'streamId', '__httpsubsonic_orgrestapi_PodcastEpisode_streamId', pyxb.binding.datatypes.string)
    __streamId._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 434, 16)
    __streamId._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 434, 16)
    
    streamId = property(__streamId.value, __streamId.set, None, None)

    
    # Attribute channelId uses Python identifier channelId
    __channelId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'channelId'), 'channelId', '__httpsubsonic_orgrestapi_PodcastEpisode_channelId', pyxb.binding.datatypes.string, required=True)
    __channelId._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 435, 16)
    __channelId._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 435, 16)
    
    channelId = property(__channelId.value, __channelId.set, None, None)

    
    # Attribute description uses Python identifier description
    __description = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'description'), 'description', '__httpsubsonic_orgrestapi_PodcastEpisode_description', pyxb.binding.datatypes.string)
    __description._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 436, 16)
    __description._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 436, 16)
    
    description = property(__description.value, __description.set, None, None)

    
    # Attribute status uses Python identifier status
    __status = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'status'), 'status', '__httpsubsonic_orgrestapi_PodcastEpisode_status', _module_typeBindings.PodcastStatus, required=True)
    __status._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 437, 16)
    __status._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 437, 16)
    
    status = property(__status.value, __status.set, None, None)

    
    # Attribute publishDate uses Python identifier publishDate
    __publishDate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'publishDate'), 'publishDate', '__httpsubsonic_orgrestapi_PodcastEpisode_publishDate', pyxb.binding.datatypes.dateTime)
    __publishDate._DeclarationLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 438, 16)
    __publishDate._UseLocation = pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 438, 16)
    
    publishDate = property(__publishDate.value, __publishDate.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __streamId.name() : __streamId,
        __channelId.name() : __channelId,
        __description.name() : __description,
        __status.name() : __status,
        __publishDate.name() : __publishDate
    })
_module_typeBindings.PodcastEpisode = PodcastEpisode
Namespace.addCategoryObject('typeBinding', 'PodcastEpisode', PodcastEpisode)


subsonic_response = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'subsonic-response'), Response, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 9, 4))
Namespace.addCategoryObject('elementBinding', subsonic_response.name().localName(), subsonic_response)



MusicFolders._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'musicFolder'), MusicFolder, scope=MusicFolders, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 75, 12)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 75, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(MusicFolders._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'musicFolder')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 75, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
MusicFolders._Automaton = _BuildAutomaton()




Indexes._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'shortcut'), Artist, scope=Indexes, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 86, 12)))

Indexes._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'index'), Index, scope=Indexes, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 87, 12)))

Indexes._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'child'), Child, scope=Indexes, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 88, 12)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 86, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 87, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 88, 12))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Indexes._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'shortcut')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 86, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Indexes._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'index')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 87, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Indexes._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'child')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 88, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Indexes._Automaton = _BuildAutomaton_()




Index._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'artist'), Artist, scope=Index, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 96, 12)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 96, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Index._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'artist')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 96, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Index._Automaton = _BuildAutomaton_2()




Genres._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'genre'), Genre, scope=Genres, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 111, 12)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 111, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Genres._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'genre')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 111, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Genres._Automaton = _BuildAutomaton_3()




def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
Genre._Automaton = _BuildAutomaton_4()




ArtistsID3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'index'), IndexID3, scope=ArtistsID3, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 122, 12)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 122, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ArtistsID3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'index')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 122, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ArtistsID3._Automaton = _BuildAutomaton_5()




IndexID3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'artist'), ArtistID3, scope=IndexID3, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 129, 12)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 129, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(IndexID3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'artist')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 129, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
IndexID3._Automaton = _BuildAutomaton_6()




Videos._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'video'), Child, scope=Videos, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 179, 12)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 179, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Videos._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'video')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 179, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Videos._Automaton = _BuildAutomaton_7()




VideoInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'captions'), Captions, scope=VideoInfo, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 185, 12)))

VideoInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'audioTrack'), AudioTrack, scope=VideoInfo, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 186, 12)))

VideoInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'conversion'), VideoConversion, scope=VideoInfo, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 187, 12)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 185, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 186, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 187, 12))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(VideoInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'captions')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 185, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(VideoInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'audioTrack')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 186, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(VideoInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'conversion')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 187, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
VideoInfo._Automaton = _BuildAutomaton_8()




NowPlaying._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'entry'), NowPlayingEntry, scope=NowPlaying, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 281, 12)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 281, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(NowPlaying._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'entry')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 281, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
NowPlaying._Automaton = _BuildAutomaton_9()




SearchResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'match'), Child, scope=SearchResult, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 299, 12)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 299, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SearchResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'match')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 299, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SearchResult._Automaton = _BuildAutomaton_10()




SearchResult2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'artist'), Artist, scope=SearchResult2, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 307, 12)))

SearchResult2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'album'), Child, scope=SearchResult2, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 308, 12)))

SearchResult2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'song'), Child, scope=SearchResult2, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 309, 12)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 307, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 308, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 309, 12))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SearchResult2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'artist')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 307, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(SearchResult2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'album')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 308, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(SearchResult2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'song')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 309, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SearchResult2._Automaton = _BuildAutomaton_11()




SearchResult3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'artist'), ArtistID3, scope=SearchResult3, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 315, 12)))

SearchResult3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'album'), AlbumID3, scope=SearchResult3, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 316, 12)))

SearchResult3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'song'), Child, scope=SearchResult3, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 317, 12)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 315, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 316, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 317, 12))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SearchResult3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'artist')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 315, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(SearchResult3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'album')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 316, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(SearchResult3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'song')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 317, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SearchResult3._Automaton = _BuildAutomaton_12()




Playlists._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'playlist'), Playlist, scope=Playlists, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 323, 12)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 323, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Playlists._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'playlist')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 323, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Playlists._Automaton = _BuildAutomaton_13()




Playlist._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'allowedUser'), pyxb.binding.datatypes.string, scope=Playlist, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 329, 12)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 329, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Playlist._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'allowedUser')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 329, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Playlist._Automaton = _BuildAutomaton_14()




ChatMessages._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'chatMessage'), ChatMessage, scope=ChatMessages, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 372, 12)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 372, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ChatMessages._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'chatMessage')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 372, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ChatMessages._Automaton = _BuildAutomaton_15()




AlbumList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'album'), Child, scope=AlbumList, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 384, 12)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 384, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AlbumList._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'album')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 384, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AlbumList._Automaton = _BuildAutomaton_16()




AlbumList2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'album'), AlbumID3, scope=AlbumList2, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 390, 12)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 390, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AlbumList2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'album')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 390, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AlbumList2._Automaton = _BuildAutomaton_17()




Songs._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'song'), Child, scope=Songs, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 396, 12)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 396, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Songs._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'song')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 396, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Songs._Automaton = _BuildAutomaton_18()




def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
Lyrics._Automaton = _BuildAutomaton_19()




Podcasts._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'channel'), PodcastChannel, scope=Podcasts, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 407, 12)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 407, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Podcasts._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'channel')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 407, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Podcasts._Automaton = _BuildAutomaton_20()




NewestPodcasts._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'episode'), PodcastEpisode, scope=NewestPodcasts, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 427, 12)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 427, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(NewestPodcasts._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'episode')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 427, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
NewestPodcasts._Automaton = _BuildAutomaton_21()




InternetRadioStations._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'internetRadioStation'), InternetRadioStation, scope=InternetRadioStations, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 456, 12)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 456, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(InternetRadioStations._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'internetRadioStation')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 456, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
InternetRadioStations._Automaton = _BuildAutomaton_22()




Bookmarks._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'bookmark'), Bookmark, scope=Bookmarks, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 469, 12)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 469, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Bookmarks._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'bookmark')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 469, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Bookmarks._Automaton = _BuildAutomaton_23()




Bookmark._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'entry'), Child, scope=Bookmark, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 475, 12)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Bookmark._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'entry')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 475, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Bookmark._Automaton = _BuildAutomaton_24()




PlayQueue._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'entry'), Child, scope=PlayQueue, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 486, 12)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 486, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(PlayQueue._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'entry')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 486, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
PlayQueue._Automaton = _BuildAutomaton_25()




Shares._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'share'), Share, scope=Shares, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 497, 12)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 497, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Shares._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'share')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 497, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Shares._Automaton = _BuildAutomaton_26()




Share._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'entry'), Child, scope=Share, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 503, 12)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 503, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Share._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'entry')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 503, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Share._Automaton = _BuildAutomaton_27()




Starred._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'artist'), Artist, scope=Starred, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 517, 12)))

Starred._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'album'), Child, scope=Starred, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 518, 12)))

Starred._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'song'), Child, scope=Starred, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 519, 12)))

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 517, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 518, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 519, 12))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Starred._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'artist')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 517, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Starred._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'album')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 518, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Starred._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'song')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 519, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Starred._Automaton = _BuildAutomaton_28()




AlbumInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'notes'), pyxb.binding.datatypes.string, scope=AlbumInfo, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 525, 12)))

AlbumInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'musicBrainzId'), pyxb.binding.datatypes.string, scope=AlbumInfo, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 526, 12)))

AlbumInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lastFmUrl'), pyxb.binding.datatypes.string, scope=AlbumInfo, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 527, 12)))

AlbumInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'smallImageUrl'), pyxb.binding.datatypes.string, scope=AlbumInfo, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 528, 12)))

AlbumInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'mediumImageUrl'), pyxb.binding.datatypes.string, scope=AlbumInfo, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 529, 12)))

AlbumInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'largeImageUrl'), pyxb.binding.datatypes.string, scope=AlbumInfo, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 530, 12)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 525, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 526, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 527, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 528, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 529, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 530, 12))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AlbumInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'notes')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 525, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AlbumInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'musicBrainzId')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 526, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(AlbumInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lastFmUrl')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 527, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(AlbumInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'smallImageUrl')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 528, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(AlbumInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'mediumImageUrl')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 529, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(AlbumInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'largeImageUrl')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 530, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AlbumInfo._Automaton = _BuildAutomaton_29()




ArtistInfoBase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'biography'), pyxb.binding.datatypes.string, scope=ArtistInfoBase, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 536, 12)))

ArtistInfoBase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'musicBrainzId'), pyxb.binding.datatypes.string, scope=ArtistInfoBase, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 537, 12)))

ArtistInfoBase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lastFmUrl'), pyxb.binding.datatypes.string, scope=ArtistInfoBase, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 538, 12)))

ArtistInfoBase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'smallImageUrl'), pyxb.binding.datatypes.string, scope=ArtistInfoBase, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 539, 12)))

ArtistInfoBase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'mediumImageUrl'), pyxb.binding.datatypes.string, scope=ArtistInfoBase, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 540, 12)))

ArtistInfoBase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'largeImageUrl'), pyxb.binding.datatypes.string, scope=ArtistInfoBase, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 541, 12)))

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 536, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 537, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 538, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 539, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 540, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 541, 12))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ArtistInfoBase._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'biography')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 536, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ArtistInfoBase._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'musicBrainzId')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 537, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ArtistInfoBase._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lastFmUrl')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 538, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ArtistInfoBase._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'smallImageUrl')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 539, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(ArtistInfoBase._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'mediumImageUrl')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 540, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(ArtistInfoBase._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'largeImageUrl')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 541, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ArtistInfoBase._Automaton = _BuildAutomaton_30()




SimilarSongs._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'song'), Child, scope=SimilarSongs, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 567, 12)))

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 567, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SimilarSongs._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'song')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 567, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SimilarSongs._Automaton = _BuildAutomaton_31()




SimilarSongs2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'song'), Child, scope=SimilarSongs2, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 573, 12)))

def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 573, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SimilarSongs2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'song')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 573, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SimilarSongs2._Automaton = _BuildAutomaton_32()




TopSongs._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'song'), Child, scope=TopSongs, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 579, 12)))

def _BuildAutomaton_33 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 579, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TopSongs._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'song')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 579, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
TopSongs._Automaton = _BuildAutomaton_33()




Starred2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'artist'), ArtistID3, scope=Starred2, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 585, 12)))

Starred2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'album'), AlbumID3, scope=Starred2, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 586, 12)))

Starred2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'song'), Child, scope=Starred2, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 587, 12)))

def _BuildAutomaton_34 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_34
    del _BuildAutomaton_34
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 585, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 586, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 587, 12))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Starred2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'artist')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 585, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Starred2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'album')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 586, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Starred2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'song')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 587, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Starred2._Automaton = _BuildAutomaton_34()




Users._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'user'), User, scope=Users, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 600, 12)))

def _BuildAutomaton_35 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_35
    del _BuildAutomaton_35
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 600, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Users._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'user')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 600, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Users._Automaton = _BuildAutomaton_35()




User._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'folder'), pyxb.binding.datatypes.int, scope=User, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 606, 12)))

def _BuildAutomaton_36 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_36
    del _BuildAutomaton_36
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 606, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(User._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'folder')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 606, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
User._Automaton = _BuildAutomaton_36()




Response._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'musicFolders'), MusicFolders, scope=Response, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 13, 12)))

Response._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'indexes'), Indexes, scope=Response, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 14, 12)))

Response._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'directory'), Directory, scope=Response, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 15, 12)))

Response._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'genres'), Genres, scope=Response, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 16, 12)))

Response._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'artists'), ArtistsID3, scope=Response, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 17, 12)))

Response._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'artist'), ArtistWithAlbumsID3, scope=Response, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 18, 12)))

Response._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'album'), AlbumWithSongsID3, scope=Response, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 19, 12)))

Response._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'song'), Child, scope=Response, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 20, 12)))

Response._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'videos'), Videos, scope=Response, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 21, 12)))

Response._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'videoInfo'), VideoInfo, scope=Response, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 22, 12)))

Response._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'nowPlaying'), NowPlaying, scope=Response, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 23, 12)))

Response._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'searchResult'), SearchResult, scope=Response, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 24, 12)))

Response._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'searchResult2'), SearchResult2, scope=Response, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 25, 12)))

Response._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'searchResult3'), SearchResult3, scope=Response, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 26, 12)))

Response._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'playlists'), Playlists, scope=Response, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 27, 12)))

Response._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'playlist'), PlaylistWithSongs, scope=Response, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 28, 12)))

Response._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'jukeboxStatus'), JukeboxStatus, scope=Response, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 29, 12)))

Response._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'jukeboxPlaylist'), JukeboxPlaylist, scope=Response, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 30, 12)))

Response._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'license'), License, scope=Response, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 31, 12)))

Response._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'users'), Users, scope=Response, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 32, 12)))

Response._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'user'), User, scope=Response, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 33, 12)))

Response._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'chatMessages'), ChatMessages, scope=Response, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 34, 12)))

Response._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'albumList'), AlbumList, scope=Response, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 35, 12)))

Response._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'albumList2'), AlbumList2, scope=Response, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 36, 12)))

Response._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'randomSongs'), Songs, scope=Response, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 37, 12)))

Response._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'songsByGenre'), Songs, scope=Response, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 38, 12)))

Response._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lyrics'), Lyrics, scope=Response, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 39, 12)))

Response._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'podcasts'), Podcasts, scope=Response, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 40, 12)))

Response._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'newestPodcasts'), NewestPodcasts, scope=Response, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 41, 12)))

Response._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'internetRadioStations'), InternetRadioStations, scope=Response, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 42, 12)))

Response._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'bookmarks'), Bookmarks, scope=Response, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 43, 12)))

Response._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'playQueue'), PlayQueue, scope=Response, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 44, 12)))

Response._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'shares'), Shares, scope=Response, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 45, 12)))

Response._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'starred'), Starred, scope=Response, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 46, 12)))

Response._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'starred2'), Starred2, scope=Response, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 47, 12)))

Response._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'albumInfo'), AlbumInfo, scope=Response, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 48, 12)))

Response._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'artistInfo'), ArtistInfo, scope=Response, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 49, 12)))

Response._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'artistInfo2'), ArtistInfo2, scope=Response, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 50, 12)))

Response._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'similarSongs'), SimilarSongs, scope=Response, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 51, 12)))

Response._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'similarSongs2'), SimilarSongs2, scope=Response, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 52, 12)))

Response._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'topSongs'), TopSongs, scope=Response, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 53, 12)))

Response._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'error'), Error, scope=Response, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 54, 12)))

def _BuildAutomaton_37 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_37
    del _BuildAutomaton_37
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 12, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Response._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'musicFolders')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 13, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Response._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'indexes')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 14, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Response._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'directory')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 15, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Response._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'genres')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 16, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Response._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'artists')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 17, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Response._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'artist')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 18, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Response._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'album')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 19, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Response._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'song')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 20, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Response._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'videos')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 21, 12))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Response._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'videoInfo')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 22, 12))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Response._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'nowPlaying')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 23, 12))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Response._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'searchResult')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 24, 12))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Response._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'searchResult2')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 25, 12))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Response._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'searchResult3')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 26, 12))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Response._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'playlists')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 27, 12))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Response._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'playlist')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 28, 12))
    st_15 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Response._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'jukeboxStatus')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 29, 12))
    st_16 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Response._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'jukeboxPlaylist')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 30, 12))
    st_17 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Response._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'license')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 31, 12))
    st_18 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Response._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'users')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 32, 12))
    st_19 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Response._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'user')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 33, 12))
    st_20 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Response._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'chatMessages')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 34, 12))
    st_21 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_21)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Response._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'albumList')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 35, 12))
    st_22 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_22)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Response._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'albumList2')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 36, 12))
    st_23 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_23)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Response._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'randomSongs')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 37, 12))
    st_24 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_24)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Response._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'songsByGenre')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 38, 12))
    st_25 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_25)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Response._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lyrics')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 39, 12))
    st_26 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_26)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Response._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'podcasts')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 40, 12))
    st_27 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_27)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Response._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'newestPodcasts')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 41, 12))
    st_28 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_28)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Response._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'internetRadioStations')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 42, 12))
    st_29 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_29)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Response._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'bookmarks')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 43, 12))
    st_30 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_30)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Response._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'playQueue')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 44, 12))
    st_31 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_31)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Response._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'shares')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 45, 12))
    st_32 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_32)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Response._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'starred')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 46, 12))
    st_33 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_33)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Response._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'starred2')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 47, 12))
    st_34 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_34)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Response._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'albumInfo')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 48, 12))
    st_35 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_35)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Response._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'artistInfo')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 49, 12))
    st_36 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_36)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Response._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'artistInfo2')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 50, 12))
    st_37 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_37)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Response._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'similarSongs')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 51, 12))
    st_38 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_38)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Response._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'similarSongs2')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 52, 12))
    st_39 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_39)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Response._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'topSongs')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 53, 12))
    st_40 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_40)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Response._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'error')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 54, 12))
    st_41 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_41)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_20._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_21._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_22._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_23._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_24._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_25._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_26._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_27._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_28._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_29._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_30._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_31._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_32._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_33._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_34._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_35._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_36._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_37._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_38._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_39._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_40._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_41._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Response._Automaton = _BuildAutomaton_37()




ArtistWithAlbumsID3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'album'), AlbumID3, scope=ArtistWithAlbumsID3, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 146, 20)))

def _BuildAutomaton_38 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_38
    del _BuildAutomaton_38
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 146, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ArtistWithAlbumsID3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'album')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 146, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ArtistWithAlbumsID3._Automaton = _BuildAutomaton_38()




AlbumWithSongsID3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'song'), Child, scope=AlbumWithSongsID3, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 171, 20)))

def _BuildAutomaton_39 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_39
    del _BuildAutomaton_39
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 171, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AlbumWithSongsID3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'song')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 171, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AlbumWithSongsID3._Automaton = _BuildAutomaton_39()




Directory._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'child'), Child, scope=Directory, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 211, 12)))

def _BuildAutomaton_40 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_40
    del _BuildAutomaton_40
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 211, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Directory._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'child')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 211, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Directory._Automaton = _BuildAutomaton_40()




PlaylistWithSongs._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'entry'), Child, scope=PlaylistWithSongs, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 347, 20)))

def _BuildAutomaton_41 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_41
    del _BuildAutomaton_41
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 329, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 347, 20))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(PlaylistWithSongs._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'allowedUser')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 329, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(PlaylistWithSongs._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'entry')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 347, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
PlaylistWithSongs._Automaton = _BuildAutomaton_41()




JukeboxPlaylist._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'entry'), Child, scope=JukeboxPlaylist, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 364, 20)))

def _BuildAutomaton_42 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_42
    del _BuildAutomaton_42
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 364, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(JukeboxPlaylist._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'entry')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 364, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
JukeboxPlaylist._Automaton = _BuildAutomaton_42()




PodcastChannel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'episode'), PodcastEpisode, scope=PodcastChannel, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 413, 12)))

def _BuildAutomaton_43 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_43
    del _BuildAutomaton_43
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 413, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(PodcastChannel._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'episode')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 413, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
PodcastChannel._Automaton = _BuildAutomaton_43()




ArtistInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'similarArtist'), Artist, scope=ArtistInfo, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 549, 20)))

def _BuildAutomaton_44 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_44
    del _BuildAutomaton_44
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 536, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 537, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 538, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 539, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 540, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 541, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 549, 20))
    counters.add(cc_6)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ArtistInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'biography')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 536, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ArtistInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'musicBrainzId')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 537, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ArtistInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lastFmUrl')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 538, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ArtistInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'smallImageUrl')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 539, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(ArtistInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'mediumImageUrl')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 540, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(ArtistInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'largeImageUrl')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 541, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(ArtistInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'similarArtist')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 549, 20))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ArtistInfo._Automaton = _BuildAutomaton_44()




ArtistInfo2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'similarArtist'), ArtistID3, scope=ArtistInfo2, location=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 559, 20)))

def _BuildAutomaton_45 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_45
    del _BuildAutomaton_45
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 536, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 537, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 538, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 539, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 540, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 541, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 559, 20))
    counters.add(cc_6)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ArtistInfo2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'biography')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 536, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ArtistInfo2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'musicBrainzId')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 537, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ArtistInfo2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lastFmUrl')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 538, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ArtistInfo2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'smallImageUrl')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 539, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(ArtistInfo2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'mediumImageUrl')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 540, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(ArtistInfo2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'largeImageUrl')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 541, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(ArtistInfo2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'similarArtist')), pyxb.utils.utility.Location('file:///c:/Dev/beets-subsonic/beetsplug/subsonic/xsd/subsonic-rest-api-1.14.0.xsd', 559, 20))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ArtistInfo2._Automaton = _BuildAutomaton_45()

