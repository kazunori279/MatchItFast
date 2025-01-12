import Action from 'Action'
import { initialAppInfo } from 'AppInfo'

function appReducer(appInfo: any, action: Action) {
    switch(action.type) {
        case "start":
            return { ...appInfo, ...{ page: "ModeSelection" } };
        case "image":
            return { ...appInfo, ...{ page: "ImageSelection", imageUrl: null, embedding: null } };
        case "reset":
            return initialAppInfo;
        case "select":
            return { ...appInfo, ...{ page: "ImageResult", selection: action.data, imageUrl: null,  } };
        case "selectImage":
            return { ...appInfo, ...{ page: "ImageResult", selection: null, imageUrl: action.data.imageUrl, embedding: action.data.embedding } };
        case "document":
            return { ...appInfo, ...{ page: "DocumentForm", documentText: null } };
        case "queryWithDocument":
            return { ...appInfo, ...{ page: "DocumentResult", documentText: action.data.text } };
    }
}

export default appReducer;

// vim:ft=typescriptreact sw=4
