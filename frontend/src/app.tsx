import {
  createBalancedTreeFromLeaves,
  getLeaves,
  Mosaic,
  MosaicBranch,
  MosaicNode,
  MosaicWindow,
  MosaicZeroState,
} from "react-mosaic-component";
import { invoke } from "@tauri-apps/api/core";
import { Classes } from "@blueprintjs/core";
import { IconNames } from "@blueprintjs/icons";
import { Children, useState } from "react";
import classNames from "classnames";

import "react-mosaic-component/react-mosaic-component.css";
import "@blueprintjs/core/lib/css/blueprint.css";
import "@blueprintjs/icons/lib/css/blueprint-icons.css";
import "./app.css";
import { CloseAdditionalControlsButton } from "./components/close-additional-controls-button";

type ViewId = "grafana" | "prometheus" | "portainer";

const TITLE_MAP: Record<ViewId, string> = {
  grafana: "Grafana",
  prometheus: "Prometheus",
  portainer: "Portainer",
};

const ELEMENT_MAP: Record<ViewId, JSX.Element> = {
  grafana: <iframe src="http://localhost:32911" id="grafana-view" />,
  prometheus: <iframe src="http://localhost:52441" id="prometheus-view" />,
  portainer: <iframe src="http://localhost:37017" id="portainer-view" />,
};

function App() {
  const [currentNode, setCurrentNode] = useState<MosaicNode<ViewId> | null>(
    null
  );

  async function quit() {
    await invoke("quit");
  }

  const onChange = (currentNode: MosaicNode<ViewId> | null) => {
    setCurrentNode(currentNode);
  };

  const onRelease = (currentNode: MosaicNode<ViewId> | null) => {
    console.log("Mosaic.onRelease():", currentNode);
  };

  const autoArrange = () => {
    const leaves = getLeaves(currentNode);
    setCurrentNode(createBalancedTreeFromLeaves(leaves));
  };

  const totalWindowCount = getLeaves(currentNode).length;

  return (
    <>
      <div
        className={classNames(
          Classes.NAVBAR,
          Classes.DARK,
          "flex",
          "justify-between"
        )}
      >
        <div className={Classes.NAVBAR_GROUP}>
          <div className={Classes.NAVBAR_HEADING}>Sys o11y</div>
        </div>
        <div className={classNames(Classes.NAVBAR_GROUP, Classes.BUTTON_GROUP)}>
          <div className="navbar-separator" />
          <button
            className={classNames(
              Classes.BUTTON,
              Classes.iconClass(IconNames.GRID_VIEW)
            )}
            onClick={autoArrange}
          >
            Auto Arrange
          </button>
          <button
            className={classNames(
              Classes.BUTTON,
              Classes.iconClass(IconNames.LogOut)
            )}
            onClick={quit}
          >
            Quit
          </button>
        </div>
      </div>
      <Mosaic<ViewId>
        renderTile={(id, path) => (
          <CustomWindow
            count={path.length}
            path={path}
            totalWindowCount={totalWindowCount}
            id={id}
          />
        )}
        zeroStateView={
          <MosaicZeroState createNode={() => totalWindowCount + 1} />
        }
        value={currentNode}
        onChange={onChange}
        onRelease={onRelease}
        className={"mosaic-blueprint-theme"}
        blueprintNamespace="bp4"
        initialValue={{
          direction: "row",
          first: "grafana",
          second: {
            direction: "column",
            first: "prometheus",
            second: "portainer",
          },
          splitPercentage: 40,
        }}
      />
    </>
  );
}

interface CustomWindowProps {
  count: number;
  path: MosaicBranch[];
  totalWindowCount: number;
  id: ViewId;
}

const additionalControls = Children.toArray([
  <CloseAdditionalControlsButton />,
]);

const CustomWindow = ({
  count,
  path,
  totalWindowCount,
  id,
}: CustomWindowProps) => {
  return (
    <MosaicWindow<number>
      additionalControls={count === 3 ? additionalControls : []}
      title={TITLE_MAP[id]}
      createNode={() => totalWindowCount + 1}
      path={path}
      onDragStart={() => console.log("MosaicWindow.onDragStart")}
      onDragEnd={(type) => console.log("MosaicWindow.onDragEnd", type)}
    >
      {ELEMENT_MAP[id]}
    </MosaicWindow>
  );
};

export default App;
