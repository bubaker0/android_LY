// Copyright (C) 2022 The Qt Company Ltd.
// SPDX-License-Identifier: LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only


#ifndef SBK_QTHELP_PYTHON_H
#define SBK_QTHELP_PYTHON_H

#include <sbkpython.h>
#include <sbkconverter.h>
// Module Includes
#include <pyside6_qtwidgets_python.h>
#include <pyside6_qtgui_python.h>
#include <pyside6_qtcore_python.h>

// Bound library includes
#include <QtHelp/qhelpsearchengine.h>
class QCompressedHelpInfo;
class QHelpContentItem;
class QHelpContentModel;
class QHelpContentWidget;
class QHelpEngine;
class QHelpEngineCore;
class QHelpFilterData;
class QHelpFilterEngine;
class QHelpFilterSettingsWidget;
class QHelpIndexModel;
class QHelpIndexWidget;
struct QHelpLink;
class QHelpSearchEngine;
class QHelpSearchQueryWidget;
class QHelpSearchResult;
class QHelpSearchResultWidget;
// Type indices
enum : int {
    SBK_QCOMPRESSEDHELPINFO_IDX                              = 0,
    SBK_QHELPCONTENTITEM_IDX                                 = 1,
    SBK_QHELPCONTENTMODEL_IDX                                = 2,
    SBK_QHELPCONTENTWIDGET_IDX                               = 3,
    SBK_QHELPENGINE_IDX                                      = 4,
    SBK_QHELPENGINECORE_IDX                                  = 5,
    SBK_QHELPFILTERDATA_IDX                                  = 6,
    SBK_QHELPFILTERENGINE_IDX                                = 7,
    SBK_QHELPFILTERSETTINGSWIDGET_IDX                        = 8,
    SBK_QHELPINDEXMODEL_IDX                                  = 9,
    SBK_QHELPINDEXWIDGET_IDX                                 = 10,
    SBK_QHELPLINK_IDX                                        = 11,
    SBK_QHELPSEARCHENGINE_IDX                                = 12,
    SBK_QHELPSEARCHQUERY_FIELDNAME_IDX                       = 14,
    SBK_QHELPSEARCHQUERY_IDX                                 = 13,
    SBK_QHELPSEARCHQUERYWIDGET_IDX                           = 15,
    SBK_QHELPSEARCHRESULT_IDX                                = 16,
    SBK_QHELPSEARCHRESULTWIDGET_IDX                          = 17,
    SBK_QtHelp_IDX_COUNT                                     = 18
};
// This variable stores all Python types exported by this module.
extern PyTypeObject **SbkPySide6_QtHelpTypes;

// This variable stores the Python module object exported by this module.
extern PyObject *SbkPySide6_QtHelpModuleObject;

// This variable stores all type converters exported by this module.
extern SbkConverter **SbkPySide6_QtHelpTypeConverters;

// Converter indices
enum : int {
    SBK_QTHELP_QLIST_INT_IDX                                 = 0, // QList<int>
    SBK_QTHELP_QLIST_QVERSIONNUMBER_IDX                      = 1, // QList<QVersionNumber>
    SBK_QTHELP_QLIST_QMODELINDEX_IDX                         = 2, // QList<QModelIndex>
    SBK_QTHELP_QLIST_QHELPLINK_IDX                           = 3, // QList<QHelpLink>
    SBK_QTHELP_QMULTIMAP_QSTRING_QURL_IDX                    = 4, // QMultiMap<QString,QUrl>
    SBK_QTHELP_QLIST_QACTIONPTR_IDX                          = 5, // QList<QAction*>
    SBK_QTHELP_QLIST_QHELPSEARCHQUERY_IDX                    = 6, // QList<QHelpSearchQuery>
    SBK_QTHELP_QLIST_QOBJECTPTR_IDX                          = 7, // QList<QObject*>
    SBK_QTHELP_QLIST_QBYTEARRAY_IDX                          = 8, // QList<QByteArray>
    SBK_QTHELP_STD_PAIR_QSTRING_QSTRING_IDX                  = 9, // std::pair<QString,QString>
    SBK_QTHELP_QLIST_STD_PAIR_QSTRING_QSTRING_IDX            = 10, // QList<std::pair< QString,QString>>
    SBK_QTHELP_QLIST_QHELPSEARCHRESULT_IDX                   = 11, // QList<QHelpSearchResult>
    SBK_QTHELP_QMAP_QSTRING_QSTRING_IDX                      = 12, // QMap<QString,QString>
    SBK_QTHELP_QMAP_QSTRING_QVERSIONNUMBER_IDX               = 13, // QMap<QString,QVersionNumber>
    SBK_QTHELP_QLIST_QURL_IDX                                = 14, // QList<QUrl>
    SBK_QTHELP_QLIST_QSTRINGLIST_IDX                         = 15, // QList<QStringList>
    SBK_QTHELP_QMAP_INT_QVARIANT_IDX                         = 16, // QMap<int,QVariant>
    SBK_QTHELP_QHASH_INT_QBYTEARRAY_IDX                      = 17, // QHash<int,QByteArray>
    SBK_QTHELP_QLIST_QVARIANT_IDX                            = 18, // QList<QVariant>
    SBK_QTHELP_QLIST_QSTRING_IDX                             = 19, // QList<QString>
    SBK_QTHELP_QMAP_QSTRING_QVARIANT_IDX                     = 20, // QMap<QString,QVariant>
    SBK_QtHelp_CONVERTERS_IDX_COUNT                          = 21
};
// Macros for type check

QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace Shiboken
{

// PyType functions, to get the PyObjectType for a type T
template<> inline PyTypeObject *SbkType< ::QCompressedHelpInfo >() { return SbkPySide6_QtHelpTypes[SBK_QCOMPRESSEDHELPINFO_IDX]; }
template<> inline PyTypeObject *SbkType< ::QHelpContentItem >() { return SbkPySide6_QtHelpTypes[SBK_QHELPCONTENTITEM_IDX]; }
template<> inline PyTypeObject *SbkType< ::QHelpContentModel >() { return SbkPySide6_QtHelpTypes[SBK_QHELPCONTENTMODEL_IDX]; }
template<> inline PyTypeObject *SbkType< ::QHelpContentWidget >() { return SbkPySide6_QtHelpTypes[SBK_QHELPCONTENTWIDGET_IDX]; }
template<> inline PyTypeObject *SbkType< ::QHelpEngine >() { return SbkPySide6_QtHelpTypes[SBK_QHELPENGINE_IDX]; }
template<> inline PyTypeObject *SbkType< ::QHelpEngineCore >() { return SbkPySide6_QtHelpTypes[SBK_QHELPENGINECORE_IDX]; }
template<> inline PyTypeObject *SbkType< ::QHelpFilterData >() { return SbkPySide6_QtHelpTypes[SBK_QHELPFILTERDATA_IDX]; }
template<> inline PyTypeObject *SbkType< ::QHelpFilterEngine >() { return SbkPySide6_QtHelpTypes[SBK_QHELPFILTERENGINE_IDX]; }
template<> inline PyTypeObject *SbkType< ::QHelpFilterSettingsWidget >() { return SbkPySide6_QtHelpTypes[SBK_QHELPFILTERSETTINGSWIDGET_IDX]; }
template<> inline PyTypeObject *SbkType< ::QHelpIndexModel >() { return SbkPySide6_QtHelpTypes[SBK_QHELPINDEXMODEL_IDX]; }
template<> inline PyTypeObject *SbkType< ::QHelpIndexWidget >() { return SbkPySide6_QtHelpTypes[SBK_QHELPINDEXWIDGET_IDX]; }
template<> inline PyTypeObject *SbkType< ::QHelpLink >() { return SbkPySide6_QtHelpTypes[SBK_QHELPLINK_IDX]; }
template<> inline PyTypeObject *SbkType< ::QHelpSearchEngine >() { return SbkPySide6_QtHelpTypes[SBK_QHELPSEARCHENGINE_IDX]; }
template<> inline PyTypeObject *SbkType< ::QHelpSearchQuery::FieldName >() { return SbkPySide6_QtHelpTypes[SBK_QHELPSEARCHQUERY_FIELDNAME_IDX]; }
template<> inline PyTypeObject *SbkType< ::QHelpSearchQuery >() { return SbkPySide6_QtHelpTypes[SBK_QHELPSEARCHQUERY_IDX]; }
template<> inline PyTypeObject *SbkType< ::QHelpSearchQueryWidget >() { return SbkPySide6_QtHelpTypes[SBK_QHELPSEARCHQUERYWIDGET_IDX]; }
template<> inline PyTypeObject *SbkType< ::QHelpSearchResult >() { return SbkPySide6_QtHelpTypes[SBK_QHELPSEARCHRESULT_IDX]; }
template<> inline PyTypeObject *SbkType< ::QHelpSearchResultWidget >() { return SbkPySide6_QtHelpTypes[SBK_QHELPSEARCHRESULTWIDGET_IDX]; }

} // namespace Shiboken

QT_WARNING_POP
#endif // SBK_QTHELP_PYTHON_H

